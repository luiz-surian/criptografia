# Set the venv folder name
$venvFolder = "criptografia-venv"


# Check if venv folder doesn't exist
if (-Not (Test-Path -Path $venvFolder)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venvFolder
}

# Activate the virtual environment
& "$venvFolder\\Scripts\\Activate.ps1"

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install jupyterlab
pip install -r requirements.txt

# Clear the console
Clear-Host

# Launch JupyterLab
jupyter lab

# Deactivate the virtual environment
deactivate
exit
