# scripts/run_app.ps1

Set-Location $PSScriptRoot\..

if (-not (Test-Path "venv")) {
    python -m venv venv
}

. .\venv\bin\Activate.ps1

pip install -r requirements.txt

python server.py