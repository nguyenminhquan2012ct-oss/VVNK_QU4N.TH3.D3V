@echo off
title VVNK - Cai dat thu vien
color 0A

echo ============================================
echo       VVNK - Cai dat thu vien
echo ============================================
echo.

python --version 2>NUL
if %errorlevel% neq 0 (
    echo [!] Python chua duoc cai dat!
    pause
    exit /b 1
)

echo [*] Dang cap nhat pip...
python -m pip install --upgrade pip

echo.
echo [*] Dang cai dat thu vien...
python install.py

echo.
echo ============================================
echo       Cai dat xong!
echo ============================================
pause
