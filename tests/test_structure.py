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
        'docs/architecture.md',
        'docs/onboarding.md',
        'docs/public-release-checklist.md',
        '.github/workflows/ci.yml',
        'pack.yaml',
        'install.sh',
        'install.ps1',
        'scripts/install_pack.py',
        'scripts/onboard.py',
        'scripts/release_check.py',
        'scripts/sanitize_check.py',
        'library-template/SCHEMA.md',
        'library-template/scripts/onboard.py',
        'library-template/scripts/sanitize_check.py',
        'profiles/librarian/config.yaml',
        'profiles/scout/config.yaml',
        'profiles/architect/config.yaml',
        'profiles/oracle/config.yaml',
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
        '--library-name', 'adaptative-living-library-test', '--install-skills'
    ], text=True, capture_output=True)
    assert r.returncode == 0, r.stdout + r.stderr
    installed = target / 'libraries' / 'adaptative-living-library-test'
    for rel in ['scripts/library_preflight.py', 'scripts/lint_library.py', 'scripts/sanitize_check.py', 'scripts/onboard.py']:
        assert (installed / rel).exists(), rel
    assert not list(installed.rglob('__pycache__'))
    assert not list(installed.rglob('*.pyc'))
    for role in ['librarian', 'scout', 'architect', 'oracle']:
        assert (target / 'skills' / 'community' / 'adaptative-living-library' / role / 'SKILL.md').exists()


def test_onboarding_generates_bind_ready_profiles_and_raw(tmp_path):
    target = tmp_path / 'hermes-home'
    vault = tmp_path / 'vault'
    vault.mkdir()
    install = subprocess.run([
        'bash', str(ROOT/'install.sh'), '--apply', '--target', str(target),
        '--library-name', 'adaptative-living-library-test', '--install-skills'
    ], text=True, capture_output=True)
    assert install.returncode == 0, install.stdout + install.stderr
    onboard = subprocess.run([
        sys.executable, str(ROOT/'scripts/onboard.py'), '--apply', '--target', str(target),
        '--library-name', 'adaptative-living-library-test', '--operator-name', 'Example Operator',
        '--provider', 'openrouter', '--main-model', 'anthropic/claude-sonnet-4',
        '--librarian-model', 'anthropic/claude-sonnet-4', '--scout-model', 'openai/gpt-4.1-mini',
        '--architect-model', 'anthropic/claude-sonnet-4', '--oracle-model', 'openai/gpt-4.1-mini',
        '--topic', 'AI agents', '--topic', 'creative video workflows',
        '--session-source', str(ROOT/'examples/sample-session.txt'),
        '--memory-source', str(ROOT/'examples/sample-memory.md'),
        '--obsidian-vault', str(vault), '--non-interactive'
    ], text=True, capture_output=True)
    assert onboard.returncode == 0, onboard.stdout + onboard.stderr
    library = target / 'libraries' / 'adaptative-living-library-test'
    assert (library / 'onboarding' / 'adaptative-config.yaml').exists()
    assert 'AI agents' in (library / 'onboarding' / 'adaptative-config.yaml').read_text()
    assert list((library / 'raw' / 'onboarding').glob('initial-discovery-*.md'))
    scout_profile = target / 'profiles' / 'scout' / 'config.yaml'
    assert scout_profile.exists()
    assert 'openai/gpt-4.1-mini' in scout_profile.read_text()
    for role in ['librarian', 'architect', 'oracle']:
        assert (target / 'profiles' / role / 'config.yaml').exists()
    assert (vault / 'Adaptative Living Library').exists() or (vault / 'ADAPTATIVE_LIVING_LIBRARY_LINK.md').exists()
