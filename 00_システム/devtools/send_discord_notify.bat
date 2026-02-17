@echo off
chcp 65001 >nul 2>&1
REM =============================================
REM Discord通知送信バッチ
REM 使い方: send_discord_notify.bat "メッセージ"
REM =============================================

cd /d "%~dp0"
if "%~1"=="" (
    set /p msg="送信するメッセージを入力してください: "
) else (
    set msg=%*
)

python discord_notify.py "%msg%"

if %ERRORLEVEL% neq 0 (
    echo.
    echo 送信に失敗しました。
    pause
) else (
    echo.
    echo 送信完了しました。（何かキーを押すと閉じます）
    pause >nul
)
