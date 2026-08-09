@echo off
title VVNK - QU4N.TH3.D3V
color 0A

echo ============================================
echo        VVNK - QU4N.TH3.D3V
echo ============================================
echo.

python --version 2>NUL
if %errorlevel% neq 0 (
    echo [!] Python chua duoc cai dat!
    pause
    exit /b 1
)

if not exist "config" mkdir config
if not exist "config\config.json" (
    echo {"token": "", "prefix": ".", "sniper_webhook": ""} > config\config.json
    echo [!] Chua co token. Mo notepad de nhap token...
    notepad config\config.json
    echo [!] Nhap token xong nhan Enter de tiep tuc...
    pause >NUL
)

if not exist "music" mkdir music
if not exist "ffmpeg" mkdir ffmpeg
if not exist "trash" mkdir trash
if not exist "cogs" mkdir cogs

echo ============================================
echo       Dang chay VVNK...
echo ============================================
echo.

:restart
python bot.py
echo.
echo [*] Da dung. Khoi dong lai sau 3 giay...
timeout /t 3 >NUL
goto restart
