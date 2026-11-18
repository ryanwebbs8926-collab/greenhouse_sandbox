# Creates .venv (if missing) and installs/updates dependencies.
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment in .venv ..."
    python -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements\dev.txt

Write-Host ""
Write-Host "Done. Activate with: .\.venv\Scripts\Activate.ps1"
