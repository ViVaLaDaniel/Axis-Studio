# --- ⚙️ AXIS SAVE (Backup Only) ---

$SourceDir = Get-Location
$ProjectName = Split-Path $SourceDir -Leaf
$BackupRoot = "G:\My Drive\Axis Projects Backup"
$BackupDir = Join-Path $BackupRoot $ProjectName

Write-Host "===== 🚀 СОХРАНЕНИЕ ПРОЕКТА: $ProjectName =====" -ForegroundColor Cyan

# 1. ОТПРАВКА НА GITHUB
if (Test-Path ".git") {
    Write-Host "🐙 GitHub..." -ForegroundColor Yellow
    $gitStatus = git status --porcelain
    if (-not [string]::IsNullOrWhiteSpace($gitStatus)) {
        git add .
        $CommitMsg = if ($args[0]) { $args[0] } else { "Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')" }
        git commit -m "$CommitMsg"
        git push origin main
    } else {
        Write-Host "ℹ️ Нет изменений для Git." -ForegroundColor Gray
    }
}

# 2. КОПИЯ НА GOOGLE ДИСК
if (Test-Path "G:\My Drive") {
    Write-Host "☁️ Google Drive..." -ForegroundColor Yellow
    if (-not (Test-Path $BackupDir)) { New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null }
    
    # Просто копируем текущую папку на диск
    $robocopyArgs = @("$SourceDir", "$BackupDir", "/MIR", "/MT:8", "/R:1", "/W:1", "/XD", ".git", "node_modules", ".idea", "/NFL", "/NDL", "/NJH", "/NJS")
    Start-Process -FilePath "robocopy" -ArgumentList $robocopyArgs -NoNewWindow -Wait
    Write-Host "✅ Бэкап на Диске обновлен." -ForegroundColor Green
}

Write-Host "🏁 Готово."
Start-Sleep -Seconds 2