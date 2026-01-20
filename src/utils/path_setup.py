from pathlib import Path
import sys

def setup_project_path():
    cwd = Path.cwd()

    project_root = next(
        p for p in [cwd] + list(cwd.parents)
        if (p / "src").exists()
    )

    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    return project_root
