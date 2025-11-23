# --- ⚙️ AXIS SAVE SYSTEM (PowerShell Edition) ---

# 1. Получаем текущую папку
$SourceDir = Get-Location
$ProjectName = Split-Path $SourceDir -Leaf

# 2. Настройки Google Диска (Предполагаем G:\)
$BackupRoot = "G:\My Drive\Axis Projects Backup"
$BackupDir = Join-Path $BackupRoot $ProjectName

Write-Host "===== 🚀 AXIS SAVE: $ProjectName =====" -ForegroundColor Cyan

# Проверка Git
if (-not (Test-Path ".git")) {
    Write-Host "⚠️ ОШИБКА: Тут нет Git-репозитория." -ForegroundColor Red
    Write-Host "Сначала создай проект через 'axis start'"
    exit
}

# --- GITHUB ---
Write-Host "-------------------------------------"
Write-Host "🐙 GitHub Status..." -ForegroundColor Yellow

$gitStatus = git status --porcelain
if ([string]::IsNullOrWhiteSpace($gitStatus)) {
    Write-Host "ℹ️ Нет изменений для Git." -ForegroundColor Gray
} else {
    git add .
    
    # --- Умный генератор названия ---
    $CommitMsg = $args[0] # Первый аргумент скрипта
    
    if ([string]::IsNullOrWhiteSpace($CommitMsg)) {
        $files = git diff --cached --name-only
        $fileCount = ($files | Measure-Object).Count
        
        if ($fileCount -eq 0) {
            $CommitMsg = "Update project"
        } elseif ($fileCount -eq 1) {
            $CommitMsg = "Update: $($files)"
        } elseif ($fileCount -le 3) {
            $fileList = $files -join ", "
            $CommitMsg = "Update: $fileList"
        } else {
            $firstFile = $files[0]
            $otherCount = $fileCount - 1
            $CommitMsg = "Update: $firstFile (+ $otherCount files)"
        }
        Write-Host "🤖 Авто-название: '$CommitMsg'" -ForegroundColor Green
    }
    
    git commit -m "$CommitMsg"
    git push origin main
}

# --- GOOGLE DRIVE (ROBOCOPY) ---
Write-Host "-------------------------------------"
Write-Host "☁️ Google Drive Sync..." -ForegroundColor Yellow

if (-not (Test-Path "G:\My Drive")) {
    Write-Host "⚠️ Диск G: не найден." -ForegroundColor Red
} else {
    if (-not (Test-Path $BackupDir)) { New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null }

    # Robocopy - это мощная команда копирования в Windows (аналог rsync)
    # /MIR - зеркалирование (удаляет лишнее)
    # /XD - исключить папки
    # /NFL /NDL - меньше спама в логах
    $robocopyArgs = @(
        "$SourceDir", "$BackupDir", "/MIR", "/MT:8", "/R:1", "/W:1", 
        "/XD", ".git", "node_modules", ".idea", ".vscode", "REPORTS",
        "/NFL", "/NDL", "/NJH", "/NJS" 
    )
    
    Start-Process -FilePath "robocopy" -ArgumentList $robocopyArgs -NoNewWindow -Wait
    
    # Robocopy возвращает коды успеха до 8. Ошибки - это 16.
    if ($LASTEXITCODE -lt 8) {
        Write-Host "✅ Бэкап успешно сохранен!" -ForegroundColor Green
    } else {
        Write-Host "❌ Ошибка копирования." -ForegroundColor Red
    }
}

Write-Host "-------------------------------------"
Start-Sleep -Seconds 2
