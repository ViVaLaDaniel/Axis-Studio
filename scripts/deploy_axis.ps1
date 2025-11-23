# --- AXIS SAVE SYSTEM (Stable) ---

$SourceDir = Get-Location
$ProjectName = Split-Path $SourceDir -Leaf

# ????????? ???? ? Google ?????
$DrivePath = "G:\My Drive"
$BackupRoot = Join-Path $DrivePath "Axis Projects Backup"

Write-Host "===== [AXIS] Saving Project: $ProjectName =====" -ForegroundColor Cyan

# --- 1. GITHUB ---
if (Test-Path ".git") {
    Write-Host "[GIT] Checking status..." -ForegroundColor Yellow
    $gitStatus = git status --porcelain
    if (-not [string]::IsNullOrWhiteSpace($gitStatus)) {
        git add .
        $CommitMsg = if ($args[0]) { $args[0] } else { "Update: 2025-11-23 20:37" }
        git commit -m "$CommitMsg"
        git push origin main
        Write-Host "[GIT] Success! Code pushed to GitHub." -ForegroundColor Green
    } else {
        Write-Host "[GIT] No changes detected." -ForegroundColor Gray
    }
} else {
    Write-Host "[GIT] Warning: Not a git repository." -ForegroundColor Red
}

# --- 2. GOOGLE DRIVE ---
# ??????? ?????????, ???? ?? ???? G
if (Test-Path $DrivePath) {
    Write-Host "[DRIVE] syncing to Google Drive..." -ForegroundColor Yellow
    
    $BackupDir = Join-Path $BackupRoot $ProjectName
    if (-not (Test-Path $BackupDir)) { New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null }
    
    $robocopyArgs = @("$SourceDir", "$BackupDir", "/MIR", "/MT:8", "/R:1", "/W:1", "/XD", ".git", "node_modules", ".idea", ".vscode", "scripts", "/NFL", "/NDL", "/NJH", "/NJS")
    Start-Process -FilePath "robocopy" -ArgumentList $robocopyArgs -NoNewWindow -Wait
    
    Write-Host "[DRIVE] Backup completed successfully." -ForegroundColor Green
} else {
    # ???? ????? ??? - ?????? ?????????????, ?? ?? ?????? ??????
    Write-Host "[DRIVE] Warning: Drive G: not found. Backup skipped." -ForegroundColor Magenta
}

Write-Host "[DONE] Finished."
Start-Sleep -Seconds 2
