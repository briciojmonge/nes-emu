param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ProgramArgs
)

if ($ProgramArgs.Count -lt 1) {
    throw "No executable path was passed by cargo runner"
}

$exePath = $ProgramArgs[0]
$exeArgs = @()
if ($ProgramArgs.Count -gt 1) {
    $exeArgs = $ProgramArgs[1..($ProgramArgs.Count - 1)]
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$sdlBinPath = Join-Path $repoRoot "external/SDL2/lib/x64"
$sdlDllPath = Join-Path $sdlBinPath "SDL2.dll"

if (-not (Test-Path $sdlDllPath)) {
    Write-Warning "SDL2.dll not found at $sdlDllPath"
    Write-Warning "Extract SDL2-devel-2.32.10-VC.zip and copy lib/x64/SDL2.dll there."
}

$env:PATH = "$sdlBinPath;$env:PATH"
& $exePath @exeArgs
exit $LASTEXITCODE
