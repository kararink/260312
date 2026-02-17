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

REM Tesseract OCRの確認
echo [2/3] Tesseract OCRの確認...
if exist "C:\Program Files\Tesseract-OCR\tesseract.exe" (
    echo Tesseract OCR: インストール済み
) else if exist "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" (
    echo Tesseract OCR: インストール済み
) else (
    echo.
    echo [重要] Tesseract OCRがインストールされていません。
    echo.
    echo 以下のURLからダウンロードしてインストールしてください：
    echo https://github.com/UB-Mannheim/tesseract/wiki
    echo.
    echo ※ インストール時に「Japanese」言語パックを選択してください
    echo ※ デフォルトのインストール先を推奨します
    echo.
    echo インストール完了後、このスクリプトを再実行してください。
    echo.
    
    set /p OPEN_URL="ダウンロードページを開きますか？ (y/n): "
    if /i "%OPEN_URL%"=="y" (
        start https://github.com/UB-Mannheim/tesseract/wiki
    )
    pause
    exit /b 1
)
echo.

REM Python依存関係のインストール
echo [3/3] Python依存関係のインストール...
echo.
pip install pyautogui pillow pytesseract pywin32

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
