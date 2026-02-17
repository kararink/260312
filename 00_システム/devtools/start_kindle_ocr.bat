@echo off
chcp 65001 > nul
title Kindle OCR Tool

echo =====================================================
echo   Kindle OCR Tool - 起動
echo =====================================================
echo.

REM Pythonの確認
python --version > nul 2>&1
if errorlevel 1 (
    echo エラー: Pythonがインストールされていません。
    echo https://www.python.org/downloads/ からインストールしてください。
    pause
    exit /b 1
)

REM スクリプトの実行
cd /d "%~dp0"
python kindle_ocr.py

exit /b 0
