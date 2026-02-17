@echo off
chcp 65001 >nul 2>&1
REM =============================================
REM LINE通知送信バッチ
REM 使い方: send_line_notify.bat "メッセージ"
REM =============================================

cd /d "%~dp0"
python line_notify.py %*

if %ERRORLEVEL% neq 0 (
    echo.
    echo 送信に失敗しました。
    pause
)
