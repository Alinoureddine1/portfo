# scripts/update_dependencies.ps1

Set-Location $PSScriptRoot\..

. .\venv\bin\Activate.ps1

python -m pip install --upgrade pip

pip list --outdated --format=freeze | ForEach-Object { $_.split('==')[0] } | ForEach-Object { pip install --upgrade $_ }

pip freeze > requirements.txt

Write-Output "Dependencies updated and requirements.txt refreshed!"