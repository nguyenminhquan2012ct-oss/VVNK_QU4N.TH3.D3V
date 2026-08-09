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
)

for /f "tokens=*" %%i in ('type config\config.json') do set "line=%%i"
echo %line% | findstr /r /c:"\"token\":\s*\"\"" >NUL 2>NUL
if %errorlevel% equ 0 (
    echo [!] Chua co token trong config!
    echo [!] Mo notepad de nhap token...
    notepad config\config.json
    echo.
    echo [!] Nhap token xong nhan Enter de tiep tuc...
    pause >NUL
)

if not exist "music" mkdir music
if not exist "ffmpeg" mkdir ffmpeg
if not exist "trash" mkdir trash
if not exist "cogs" mkdir cogs

echo.
echo [*] Dang cap nhat pip...
python -m pip install --upgrade pip 2>NUL

echo.
echo [*] Dang cai dat thu vien...
python install.py

echo.
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
