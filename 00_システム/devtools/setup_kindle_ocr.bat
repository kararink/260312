@echo off
chcp 65001 > nul
title Kindle OCR Tool - セットアップ

echo =====================================================
echo   Kindle OCR Tool - 初回セットアップ
echo =====================================================
echo.

REM 管理者権限の確認
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [注意] 管理者権限がありません。
    echo Tesseract OCRのインストールには管理者権限が必要な場合があります。
    echo.
)

REM Pythonの確認
python --version > nul 2>&1
if errorlevel 1 (
    echo [エラー] Pythonがインストールされていません。
    echo.
    echo 以下のURLからPythonをインストールしてください：
    echo https://www.python.org/downloads/
    echo.
    echo ※ インストール時に「Add Python to PATH」にチェックを入れてください
    pause
    exit /b 1
)

echo [1/3] Python確認OK
python --version
echo.

REM Gemini API Requirement check
echo [2/3] APIキー用の.envファイルの確認...
if not exist ".env" (
    echo [注意] .envファイルが見つかりません。
    echo 実行にはGEMINI_API_KEYの設定が必要です。
) else (
    echo .envファイル: 存在します
)
echo.

REM Python依存関係のインストール
echo [3/3] Python依存関係のインストール...
echo.
pip install pyautogui pillow pywin32 google-generativeai python-dotenv

if errorlevel 1 (
    echo.
    echo [エラー] 依存関係のインストールに失敗しました。
    pause
    exit /b 1
)

echo.
echo =====================================================
echo   セットアップ完了！
echo =====================================================
echo.
echo start_kindle_ocr.bat をダブルクリックして起動できます。
echo.
pause
