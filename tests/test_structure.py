from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_required_paths_exist():
    for rel in ['README.md', 'pack.yaml', 'install.sh', 'scripts/install_pack.py', 'library-template/SCHEMA.md', 'profiles/ops-librarian/config.yaml']:
        assert (ROOT / rel).exists(), rel


def test_sanitizer_passes():
    r = subprocess.run([sys.executable, str(ROOT/'scripts/sanitize_check.py'), str(ROOT)], text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_library_lint_passes():
    r = subprocess.run([sys.executable, str(ROOT/'scripts/lint_library.py'), str(ROOT/'library-template')], text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr
