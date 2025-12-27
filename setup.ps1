$ScriptPath = $PSScriptRoot
$CommandName = "zyt"

Write-Host "Installing $CommandName for Windows..." -ForegroundColor Cyan

# 1. Add current folder to User PATH
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($UserPath -split ';' -notcontains $ScriptPath) {
    [Environment]::SetEnvironmentVariable("Path", "$UserPath;$ScriptPath", "User")
}

# 2. Ensure .PY files are treated as executables
$PathExt = [Environment]::GetEnvironmentVariable("PATHEXT", "User")
if ($PathExt -split ';' -notcontains ".PY") {
    [Environment]::SetEnvironmentVariable("PATHEXT", "$PathExt;.PY", "User")
}

# 3. Cleanup: Remove the Bash setup file
if (Test-Path "setup.sh") {
    Remove-Item "setup.sh"
    Write-Host "Removed Linux setup file."
}

Write-Host "Installation complete! RESTART your terminal and try running: $CommandName" -ForegroundColor Green
