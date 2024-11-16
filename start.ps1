Write-Host "This is Amin's GPT App"

# ActivateVirtualEnv.ps1

# Path to the virtual environment
$virtualEnvPath = ".\.venv" 

# Check if the virtual environment exists
if (Test-Path $virtualEnvPath) {
    # Activate the virtual environment
    $activateScript = Join-Path $virtualEnvPath "Scripts\Activate"
    if (Test-Path $activateScript) {
        Write-Host "Activating virtual environment..."
        . $activateScript
        Write-Host "Virtual environment activated."
    } else {
        Write-Host "Error: Activate script not found in the virtual environment."
    }
} else {
    Write-Host "Error: Virtual environment folder not found in the current directory."
}



# InstallPackages.ps1

# Path to the requirements.txt file
$requirementsFile = ".\requirements.txt"

# Check if requirements.txt file exists
if (Test-Path $requirementsFile) {
    # Read the content of requirements.txt and install packages
    Get-Content $requirementsFile | ForEach-Object {
        $packageName = $_.Trim()
        if ($packageName -ne "") {
            Write-Host "Installing $packageName..."
            pip install $packageName
        }
    }
    Write-Host "Packages installation complete."
} else {
    Write-Host "Error: requirements.txt not found in the current directory."
}

Write-Host "Please open this link in a browser http://127.0.0.1:8000"
$url = "http://127.0.0.1:8000"
Start-Process $url

# uvicorn command
uvicorn app.app:app --reload

