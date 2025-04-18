# w.ps1 - PowerShell script to control bots

param([int]$botCount)

Write-Host "[PowerShell] Starting the bot army!" -ForegroundColor Cyan
Write-Host "[PowerShell] Number of bots to spawn: $botCount" -ForegroundColor Yellow

# Function to simulate moving the bot
function Move-Bot {
    Write-Host "[PowerShell] Moving bot!" -ForegroundColor Green
    Start-Sleep -Seconds 2  # Simulate a delay for bot movement
}

# Function to register the bot
function Register-Bot {
    param([string]$username)
    Write-Host "[PowerShell] Registering bot with username: $username" -ForegroundColor Blue
    Start-Sleep -Seconds 2  # Simulate registration process
}

# Function to log in to the server
function Login-Bot {
    param([string]$username, [string]$password)
    Write-Host "[PowerShell] Logging in with username: $username and password: $password" -ForegroundColor Green
    Start-Sleep -Seconds 2  # Simulate login process
}

# Loop to spawn multiple bots based on the input count
for ($i = 1; $i -le $botCount; $i++) {
    Write-Host "[PowerShell] Starting bot $i of $botCount" -ForegroundColor Cyan
    Move-Bot
    Register-Bot "bot_user_$i"
    Login-Bot "bot_user_$i" "8000! 8000!"
    Move-Bot
    Write-Host "[PowerShell] Bot $i actions completed!" -ForegroundColor Magenta
}

Write-Host "[PowerShell] Bot actions completed for all bots!" -ForegroundColor Magenta