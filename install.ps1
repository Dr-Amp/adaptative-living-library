param(
  [switch]$DryRun,
  [switch]$Apply,
  [string]$Target = "$HOME/.hermes",
  [string]$LibraryName = "living-ops",
  [string]$OperatorName = "Operator"
)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$argsList = @("$ScriptDir/scripts/install_pack.py", "--target", $Target, "--library-name", $LibraryName, "--operator-name", $OperatorName)
if ($DryRun) { $argsList += "--dry-run" }
if ($Apply) { $argsList += "--apply" }
python @argsList
