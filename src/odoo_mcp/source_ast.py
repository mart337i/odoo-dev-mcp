from __future__ import annotations

import ast
import os
import re
from pathlib import Path
from typing import Any


ODOO_VERSION_PATTERN = re.compile(r"(?<!\d)(\d{2}\.0)(?!\d)")
SKIP_DIRS = {".git", ".hg", ".svn", ".venv", "venv", "__pycache__", "node_modules", "dist", "build"}


def inspect_odoo_source_content(
    path: str = "",
    query: str = "",
    scope: str = "both",
    max_files: int = 200,
    env_source: str = "",
) -> str:
    """Return a compact AST-derived summary of Odoo core/addon source."""
    roots = candidate_roots(path, env_source)
    if not roots:
        return "# Odoo Source Inspection\n\nNo path provided and `ODOO_SOURCE` is not configured."

    max_files = max(1, min(int(max_files or 200), 1000))
    scope = scope if scope in {"core", "addons", "both"} else "both"
    query_text = query.strip().lower()

    version_signals = []
    manifests = []
    syntax_errors = []
    py_candidates = []
    seen_files: set[str] = set()

    include_core = scope in {"core", "both"}
    include_addons = scope in {"addons", "both"}

    if include_core:
        for root in source_roots(roots):
            version_signals.extend(read_release_versions(root))
            for file_path in core_python_candidates(root, bool(query_text)):
                add_candidate(py_candidates, seen_files, file_path, "core")

    if include_addons:
        for root in roots:
            for manifest_file in iter_files(root, "__manifest__.py"):
                manifest = read_manifest(manifest_file)
                if manifest:
                    item = summarize_manifest(manifest_file, manifest)
                    if matches_query(item, query_text):
                        manifests.append(item)
                    for file_path in iter_files(manifest_file.parent, "*.py"):
                        add_candidate(py_candidates, seen_files, file_path, "addon")
                else:
                    syntax_errors.append(f"{manifest_file}: could not parse manifest literal")

    inspected_files = 0
    skipped_by_limit = 0
    python_summaries = []
    for file_path, source_kind in py_candidates:
        if inspected_files >= max_files:
            skipped_by_limit += 1
            continue
        inspected_files += 1
        summary = summarize_python_file(file_path, source_kind)
        if summary.get("syntax_error"):
            syntax_errors.append(f"{file_path}: {summary['syntax_error']}")
            continue
        if matches_query(summary, query_text):
            python_summaries.append(summary)

    return format_report(
        roots=roots,
        scope=scope,
        query=query,
        max_files=max_files,
        inspected_files=inspected_files,
        skipped_by_limit=skipped_by_limit,
        version_signals=version_signals,
        manifests=manifests,
        python_summaries=python_summaries,
        syntax_errors=syntax_errors,
    )


def candidate_roots(path: str, env_source: str) -> list[Path]:
    raw_roots = [value for value in [path.strip(), env_source.strip()] if value]
    roots = []
    seen = set()
    for value in raw_roots:
        root = Path(value).expanduser()
        try:
            key = str(root.resolve())
        except OSError:
            key = str(root)
        if key not in seen:
            seen.add(key)
            roots.append(root)
    return roots


def source_roots(roots: list[Path]) -> list[Path]:
    expanded = []
    for root in roots:
        expanded.append(root)
        if not root.is_dir():
            continue
        try:
            children = sorted(root.iterdir(), key=lambda child: child.name)
        except OSError:
            continue
        for child in children:
            if child.is_dir() and ((child / "odoo-bin").exists() or child.name.startswith("odoo")):
                expanded.append(child)
    unique = []
    seen = set()
    for root in expanded:
        try:
            key = str(root.resolve())
        except OSError:
            key = str(root)
        if key not in seen:
            seen.add(key)
            unique.append(root)
    return unique


def iter_files(root: Path, pattern: str):
    if not root.is_dir():
        return
    for current_root, dirs, files in os.walk(root):
        dirs[:] = sorted(directory for directory in dirs if directory not in SKIP_DIRS)
        current = Path(current_root)
        if pattern == "__manifest__.py":
            if "__manifest__.py" in files:
                yield current / "__manifest__.py"
        elif pattern == "*.py":
            for file_name in sorted(files):
                if file_name.endswith(".py"):
                    yield current / file_name


def normalize_version(value: Any) -> str:
    text = str(value).strip()
    match = ODOO_VERSION_PATTERN.search(text)
    if match:
        return match.group(1)
    if text.isdigit() and len(text) == 2:
        return f"{text}.0"
    return ""


def literal_assignments(file_path: Path, names: set[str]) -> dict[str, Any]:
    try:
        tree = ast.parse(file_path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return {}
    values = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in names:
                try:
                    values[target.id] = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    continue
    return values


def read_release_versions(root: Path) -> list[dict[str, str]]:
    signals = []
    for release_file in [root / "odoo" / "release.py", root / "release.py"]:
        if not release_file.exists():
            continue
        values = literal_assignments(release_file, {"version", "server_version", "version_info"})
        version = normalize_version(values.get("version", "")) or normalize_version(values.get("server_version", ""))
        version_info = values.get("version_info")
        if not version and isinstance(version_info, (list, tuple)) and len(version_info) >= 2:
            version = normalize_version(f"{version_info[0]}.{version_info[1]}")
        if version:
            signals.append({"version": version, "file": str(release_file)})
    return signals


def core_python_candidates(root: Path, include_query_scan: bool) -> list[Path]:
    odoo_dir = root / "odoo"
    candidates = [
        odoo_dir / "release.py",
        odoo_dir / "models.py",
        odoo_dir / "fields.py",
        odoo_dir / "http.py",
        odoo_dir / "service" / "common.py",
    ]
    found = [path for path in candidates if path.exists()]
    if include_query_scan and odoo_dir.is_dir():
        for file_path in iter_files(odoo_dir, "*.py"):
            if f"{os.sep}addons{os.sep}" in str(file_path):
                continue
            found.append(file_path)
    return found


def add_candidate(candidates: list[tuple[Path, str]], seen: set[str], file_path: Path, source_kind: str) -> None:
    try:
        key = str(file_path.resolve())
    except OSError:
        key = str(file_path)
    if key in seen:
        return
    seen.add(key)
    candidates.append((file_path, source_kind))


def read_manifest(manifest_file: Path) -> dict[str, Any] | None:
    try:
        value = ast.literal_eval(manifest_file.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, ValueError, TypeError, UnicodeDecodeError):
        return None
    return value if isinstance(value, dict) else None


def summarize_manifest(manifest_file: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "manifest",
        "file": str(manifest_file),
        "module": manifest_file.parent.name,
        "name": manifest.get("name", ""),
        "version": manifest.get("version", ""),
        "depends": manifest.get("depends", []),
        "data_count": len(manifest.get("data", []) or []),
        "installable": manifest.get("installable", True),
    }


def summarize_python_file(file_path: Path, source_kind: str) -> dict[str, Any]:
    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except SyntaxError as exc:
        return {"file": str(file_path), "source_kind": source_kind, "syntax_error": f"line {exc.lineno}: {exc.msg}"}
    except (OSError, UnicodeDecodeError) as exc:
        return {"file": str(file_path), "source_kind": source_kind, "syntax_error": str(exc)}

    summary: dict[str, Any] = {
        "kind": "python",
        "file": str(file_path),
        "source_kind": source_kind,
        "imports": [],
        "models": [],
        "controllers": [],
        "classes": [],
        "functions": [],
    }
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            summary["imports"].extend(import_names(node))
        elif isinstance(node, ast.ClassDef):
            class_summary = summarize_class(node)
            summary["classes"].append(node.name)
            if class_summary["model_name"] or class_summary["inherit"] or class_summary["fields"] or class_summary["api_methods"]:
                summary["models"].append(class_summary)
            if class_summary["routes"]:
                summary["controllers"].append(class_summary)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            summary["functions"].append(node.name)
    return summary


def import_names(node: ast.Import | ast.ImportFrom) -> list[str]:
    if isinstance(node, ast.Import):
        return [alias.name for alias in node.names]
    module = node.module or ""
    return [f"{module}.{alias.name}" if module else alias.name for alias in node.names]


def summarize_class(node: ast.ClassDef) -> dict[str, Any]:
    summary = {
        "class": node.name,
        "bases": [expr_name(base) for base in node.bases if expr_name(base)],
        "model_name": "",
        "inherit": [],
        "description": "",
        "fields": [],
        "api_methods": [],
        "routes": [],
    }
    for stmt in node.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            target = stmt.targets[0].id
            if target == "_name":
                summary["model_name"] = literal_string(stmt.value)
            elif target == "_inherit":
                summary["inherit"] = literal_string_list(stmt.value)
            elif target == "_description":
                summary["description"] = literal_string(stmt.value)
            elif is_fields_call(stmt.value):
                summary["fields"].append(target)
        elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
            decorators = [decorator_name(decorator) for decorator in stmt.decorator_list]
            api_decorators = [decorator for decorator in decorators if decorator.startswith("api.") or stmt.name.startswith(("_compute_", "_onchange_", "_check_"))]
            if api_decorators:
                summary["api_methods"].append({"method": stmt.name, "decorators": api_decorators})
            for decorator in stmt.decorator_list:
                route = route_info(stmt.name, decorator)
                if route:
                    summary["routes"].append(route)
    return summary


def expr_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = expr_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return ""


def literal_string(node: ast.AST) -> str:
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else ""


def literal_string_list(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, (ast.List, ast.Tuple)):
        return [literal_string(item) for item in node.elts if literal_string(item)]
    return []


def is_fields_call(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "fields"
    )


def decorator_name(node: ast.AST) -> str:
    target = node.func if isinstance(node, ast.Call) else node
    return expr_name(target)


def route_info(method_name: str, decorator: ast.AST) -> dict[str, Any] | None:
    if not isinstance(decorator, ast.Call) or decorator_name(decorator) not in {"http.route", "route"}:
        return None
    paths = []
    if decorator.args:
        first = decorator.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            paths = [first.value]
        elif isinstance(first, (ast.List, ast.Tuple)):
            paths = literal_string_list(first)
    kwargs = {}
    for keyword in decorator.keywords:
        if keyword.arg:
            try:
                kwargs[keyword.arg] = ast.literal_eval(keyword.value)
            except (ValueError, TypeError):
                kwargs[keyword.arg] = expr_name(keyword.value) or "<dynamic>"
    return {"method": method_name, "paths": paths, "kwargs": kwargs}


def matches_query(value: Any, query: str) -> bool:
    if not query:
        return True
    return query in str(value).lower()


def format_report(
    roots: list[Path],
    scope: str,
    query: str,
    max_files: int,
    inspected_files: int,
    skipped_by_limit: int,
    version_signals: list[dict[str, str]],
    manifests: list[dict[str, Any]],
    python_summaries: list[dict[str, Any]],
    syntax_errors: list[str],
) -> str:
    lines = [
        "# Odoo Source Inspection",
        "",
        f"Roots: {', '.join(f'`{root}`' for root in roots)}",
        f"Scope: `{scope}`",
        f"Query: `{query or '<none>'}`",
        f"Python files inspected: {inspected_files} (max {max_files})",
    ]
    if skipped_by_limit:
        lines.append(f"Files skipped by limit: {skipped_by_limit}")
    lines.extend(["", "## Version Signals"])
    lines.extend(format_version_signals(version_signals))
    lines.extend(["", "## Addon Manifests"])
    lines.extend(format_manifests(manifests))
    lines.extend(["", "## Models"])
    lines.extend(format_models(python_summaries))
    lines.extend(["", "## Controllers"])
    lines.extend(format_controllers(python_summaries))
    lines.extend(["", "## Core / Other Python Signals"])
    lines.extend(format_python_overview(python_summaries))
    lines.extend(["", "## Parse Issues"])
    lines.extend([f"- {error}" for error in syntax_errors[:20]] or ["- None"])
    lines.extend(["", "## Suggested Next Reads"])
    lines.extend(suggest_next_reads(python_summaries, manifests))
    return "\n".join(lines)


def format_version_signals(signals: list[dict[str, str]]) -> list[str]:
    if not signals:
        return ["- None found"]
    return [f"- `{signal['version']}` from `{signal['file']}`" for signal in signals]


def format_manifests(manifests: list[dict[str, Any]]) -> list[str]:
    if not manifests:
        return ["- None found"]
    lines = []
    for manifest in manifests[:30]:
        depends = manifest.get("depends", [])
        lines.append(
            f"- `{manifest['module']}`: name={manifest.get('name')!r}, version={manifest.get('version')!r}, "
            f"depends={depends}, data_files={manifest.get('data_count')}, file=`{manifest['file']}`"
        )
    if len(manifests) > 30:
        lines.append(f"- ... {len(manifests) - 30} more manifests omitted")
    return lines


def format_models(summaries: list[dict[str, Any]]) -> list[str]:
    lines = []
    for summary in summaries:
        for model in summary.get("models", []):
            header_bits = [f"class `{model['class']}`"]
            if model.get("model_name"):
                header_bits.append(f"_name=`{model['model_name']}`")
            if model.get("inherit"):
                header_bits.append(f"_inherit={model['inherit']}")
            lines.append(f"- `{summary['file']}`: " + ", ".join(header_bits))
            if model.get("fields"):
                lines.append(f"  fields: {', '.join(model['fields'][:20])}")
            if model.get("api_methods"):
                methods = [f"{item['method']} ({', '.join(item['decorators'])})" for item in model["api_methods"][:10]]
                lines.append(f"  methods: {'; '.join(methods)}")
    return lines or ["- None found"]


def format_controllers(summaries: list[dict[str, Any]]) -> list[str]:
    lines = []
    for summary in summaries:
        for controller in summary.get("controllers", []):
            for route in controller.get("routes", []):
                lines.append(
                    f"- `{summary['file']}`: `{controller['class']}.{route['method']}` "
                    f"routes={route.get('paths', [])} kwargs={route.get('kwargs', {})}"
                )
    return lines or ["- None found"]


def format_python_overview(summaries: list[dict[str, Any]]) -> list[str]:
    lines = []
    for summary in summaries:
        if summary.get("models") or summary.get("controllers"):
            continue
        classes = summary.get("classes", [])[:10]
        functions = summary.get("functions", [])[:10]
        imports = summary.get("imports", [])[:8]
        if classes or functions or imports:
            lines.append(f"- `{summary['file']}`: classes={classes}, functions={functions}, imports={imports}")
    return lines or ["- None found"]


def suggest_next_reads(summaries: list[dict[str, Any]], manifests: list[dict[str, Any]]) -> list[str]:
    files = []
    for summary in summaries:
        if summary.get("models") or summary.get("controllers"):
            files.append(summary["file"])
    files.extend(manifest["file"] for manifest in manifests[:5])
    unique = []
    seen = set()
    for file_path in files:
        if file_path not in seen:
            seen.add(file_path)
            unique.append(file_path)
    return [f"- `{file_path}`" for file_path in unique[:10]] or ["- No specific next reads suggested"]
