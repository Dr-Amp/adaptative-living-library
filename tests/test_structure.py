from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_required_paths_exist():
    required = [
        'README.md',
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'SECURITY.md',
        'docs/public-release-checklist.md',
        '.github/workflows/ci.yml',
        'pack.yaml',
        'install.sh',
        'install.ps1',
        'scripts/install_pack.py',
        'scripts/release_check.py',
        'scripts/sanitize_check.py',
        'library-template/SCHEMA.md',
        'library-template/scripts/sanitize_check.py',
        'profiles/ops-librarian/config.yaml',
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel


def test_sanitizer_passes():
    r = subprocess.run([sys.executable, str(ROOT/'scripts/sanitize_check.py'), str(ROOT)], text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_library_lint_passes():
    r = subprocess.run([sys.executable, str(ROOT/'scripts/lint_library.py'), str(ROOT/'library-template')], text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_installed_template_contains_runtime_scripts(tmp_path):
    target = tmp_path / 'hermes-home'
    r = subprocess.run([
        'bash', str(ROOT/'install.sh'), '--apply', '--target', str(target),
        '--library-name', 'living-ops-test', '--install-skills'
    ], text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr
    installed = target / 'libraries' / 'living-ops-test'
    for rel in ['scripts/library_preflight.py', 'scripts/lint_library.py', 'scripts/sanitize_check.py']:
        assert (installed / rel).exists(), rel
    assert not list(installed.rglob('__pycache__'))
    assert not list(installed.rglob('*.pyc'))
    assert (target / 'skills' / 'community' / 'living-ops' / 'ops-librarian' / 'SKILL.md').exists()
