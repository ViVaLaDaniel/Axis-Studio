# --- AXIS SAVE SYSTEM (Smart Drive + Reports) ---

$SourceDir = Get-Location
$ProjectName = Split-Path $SourceDir -Leaf

# === УМНЫЙ ПОИСК ДИСКА (Smart Discovery) ===
# Мы проверяем оба варианта, чтобы скрипт работал всегда
$DrivePath = $null
$Candidates = @("G:\My Drive", "G:\Мой диск")

foreach ($path in $Candidates) {
    if (Test-Path $path) {
        $DrivePath = $path
        break
    }
}

Write-Host "===== [AXIS] Project: $ProjectName =====" -ForegroundColor Cyan

# --- 0. ОТЧЕТЫ (REPORTS) ---
Write-Host "[REP] Generating reports..." -ForegroundColor Yellow
$ReportsDir = Join-Path $SourceDir "REPORTS"
if (-not (Test-Path $ReportsDir)) { New-Item -ItemType Directory -Force -Path $ReportsDir | Out-Null }

$DateStr = Get-Date -Format "yyyy-MM-dd"
$TimeStr = Get-Date -Format "HH:mm"
$ReportName = "REPORT_$DateStr.md"
$ReportPath = Join-Path $ReportsDir $ReportName

$GitStatus = git status --short
if ([string]::IsNullOrWhiteSpace($GitStatus)) {
    Write-Host "[REP] No changes detected. Report skipped." -ForegroundColor Gray
} else {
    $GitDiff = git diff --stat
    $FullReport = "## Axis Update: $DateStr $TimeStr

### 📂 Files:
``n$GitStatus
``n### 📊 Stats:
``n$GitDiff
``n---
*Axis CLI*"
    
    # Сохраняем отчет в UTF8
    Add-Content -Path $ReportPath -Value $FullReport -Encoding UTF8
    Write-Host "[REP] Report saved: REPORTS/$ReportName" -ForegroundColor Green

    # Ссылка в README
    $ReadmePath = Join-Path $SourceDir "README.md"
    $ReadmeEntry = "- **$DateStr $TimeStr**: [View Report](REPORTS/$ReportName)"
    if (Test-Path $ReadmePath) {
        Add-Content -Path $ReadmePath -Value $ReadmeEntry -Encoding UTF8
        Write-Host "[REP] README updated." -ForegroundColor Green
    }
}

# --- 1. GITHUB ---
if (Test-Path ".git") {
    Write-Host "[GIT] Syncing..." -ForegroundColor Yellow
    $st = git status --porcelain
    if (-not [string]::IsNullOrWhiteSpace($st)) {
        git add .
        $Msg = if ($args[0]) { $args[0] } else { "Update: $DateStr $TimeStr" }
        git commit -m "$Msg"
        git push origin main
        Write-Host "[GIT] Pushed to GitHub." -ForegroundColor Green
    }
}

# --- 2. GOOGLE DRIVE ---
if ($DrivePath) {
    Write-Host "[CLOUD] Found Drive at: $DrivePath" -ForegroundColor Yellow
    $BackupRoot = Join-Path $DrivePath "Axis Projects Backup"
    $BackupDir = Join-Path $BackupRoot $ProjectName
    
    if (-not (Test-Path $BackupDir)) { New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null }
    
    # Робокопирование
    $robocopyArgs = @("$SourceDir", "$BackupDir", "/MIR", "/MT:8", "/R:1", "/W:1", "/XD", ".git", "node_modules", ".idea", ".vscode", "scripts", "/NFL", "/NDL", "/NJH", "/NJS")
    Start-Process -FilePath "robocopy" -ArgumentList $robocopyArgs -NoNewWindow -Wait
    Write-Host "[CLOUD] Backup Complete!" -ForegroundColor Green
} else {
    Write-Host "[CLOUD] Warning: Google Drive (G:) not found." -ForegroundColor Red
    Write-Host "Check if Google Drive for Desktop is running." -ForegroundColor Gray
}

Write-Host "[DONE] Finished."
Start-Sleep -Seconds 2
