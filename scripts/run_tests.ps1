# scripts/run_tests.ps1

Set-Location $PSScriptRoot\..

. .\venv\bin\Activate.ps1

python -m unittest discover tests