#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kindle OCR Tool (High Precision Edition)
著作権法第30条に基づく私的使用目的の複製ツール
"""

import os
import sys
import time
import io
import logging
from datetime import datetime
from pathlib import Path

# gRPC/protobufの不要な警告ログを抑制
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
logging.getLogger("google").setLevel(logging.ERROR)
logging.getLogger("grpc").setLevel(logging.ERROR)

try:
    import pyautogui
    from PIL import Image
    import google.generativeai as genai
    from dotenv import load_dotenv
    import win32gui
    import win32con
    HAS_WIN32 = True
except ImportError as e:
    print(f"エラー: 必要なライブラリが見つかりません: {e}")
    print("setup_kindle_ocr.bat を実行してください。")
    input("Enterキーで終了...")
    sys.exit(1)

# 環境変数の読み込み
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def setup_gemini():
    if not GEMINI_API_KEY:
        print("エラー: GEMINI_API_KEY が .env に設定されていません。")
        print(f"[{env_path}] に GEMINI_API_KEY=あなたのキー を追記してください。")
        return False
    genai.configure(api_key=GEMINI_API_KEY)
    return True

def postprocess_text(text):
    """OCRのよくある誤認識（文字化け）を辞書ベースで置換補正する"""
    replacements = {
        # 典型的な誤読パターン
        "粟田": "栗田",
        "周五朗": "周五郎",
        "朗読": "朗読", # "朗"を全て"郎"に変えないための防波堤（必要に応じて）
        "~": "〜", # 波線
        "| ": "", # 不要な縦線の除去
        " \n": "\n", # 行末スペースの除去
    }
    
    corrected_text = text
    for old, new in replacements.items():
        corrected_text = corrected_text.replace(old, new)
        
    return corrected_text

def find_kindle_window():
    """Kindleウィンドウを探す（自分自身は除外）"""
    if not HAS_WIN32: return None
    kindle_hwnd = None
    
    def callback(hwnd, extra):
        nonlocal kindle_hwnd
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            # 自分自身や無関係なウィンドウを除外
            if ('Kindle' in title or 'kindle' in title) and 'OCR' not in title and '.py' not in title:
                kindle_hwnd = hwnd
                return False
        return True
    
    try:
        win32gui.EnumWindows(callback, None)
    except:
        pass
    return kindle_hwnd

def capture_target():
    """Kindleウィンドウ、なければ画面全体をキャプチャ"""
    hwnd = find_kindle_window()
    if hwnd:
        try:
            rect = win32gui.GetWindowRect(hwnd)
            x, y, x2, y2 = rect
            # Win10/11の不可視枠対策（少し内側を撮る）
            margin = 8
            w = (x2 - x) - (margin * 2)
            h = (y2 - y) - (margin * 2) - 8 # 下部も少し調整
            
            # ウィンドウをアクティブ化
            try:
                win32gui.SetForegroundWindow(hwnd)
                time.sleep(0.2) 
            except:
                pass

            return pyautogui.screenshot(region=(x + margin, y + margin, w, h))
        except:
            pass
    return pyautogui.screenshot()

def extract_text_with_gemini(image):
    """Gemini APIを使用して画像からテキストを高精度に抽出する"""
    try:
        # モデルの初期化 (Gemini 2.5 Flashが高速で最適)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = (
            "提供された画像に含まれる文章を、一言一句正確に文字起こししてください。"
            "縦書き、横書き、ルビ（フリガナ）、複雑なレイアウトであっても、意味が通るように自然なテキストテキストとして出力してください。"
            "ページ番号やKindleのUI（ツールバーなど）のシステム文字は除外して、本文のみを抽出してください。"
            "出力は抽出したテキストのみとし、説明や挨拶は絶対に含めないでください。"
        )
        
        response = model.generate_content([prompt, image])
        return response.text.strip()
    except Exception as e:
        return f"[Gemini API Error] {e}"

def main():
    if not setup_gemini():
        input("Enterキーで終了...")
        return

    print("="*60)
    print("  Kindle OCR Tool - Gemini Vision Edition")
    print("="*60)
    print("  AI (Gemini) の視覚機能を使用して画像を解析します。")
    print("  縦書きや複雑なレイアウトも高精度に文字起こしします。")
    print("-" * 60)

    # 同意確認
    if input("  私的使用目的ですか？ (y/n): ").lower() != 'y':
        return

    title = input("\n  書籍タイトル: ").strip() or "無題"
    
    # 保存先
    base_dir = Path(__file__).parent.parent.parent / "99_Sbox" / "書籍OCR"
    base_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n  保存先: {base_dir}")
    print("-" * 60)
    print("  【操作方法】")
    print("  s + Enter : 3秒後にキャプチャ＆OCR")
    print("  q + Enter : 保存して終了")
    print("=" * 60)

    pages = []
    
    while True:
        cmd = input(f"\n[Page {len(pages)+1}] Command (s/q): ").strip().lower()
        
        if cmd == 'q':
            if not pages:
                print("  → 保存するページがありません")
                break
            
            # 保存処理
            safe_title = "".join(c if c.isalnum() else '_' for c in title)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{safe_title}_{timestamp}.md"
            path = base_dir / filename
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                for i, p in enumerate(pages, 1):
                    f.write(f"## Page {i}\n\n{p}\n\n")
                f.write(f"---\nGenerated: {datetime.now()}")
            
            print(f"\n  保存完了！\n  File: {path}")
            break
            
        elif cmd == 's':
            print("\n  準備... Kindleを開いてください (3秒待機)")
            for i in range(3, 0, -1):
                print(f"  {i}...", end="\r")
                time.sleep(1)
            
            print("  📸 キャプチャ中...", end="\r")
            img = capture_target()
            
            print("  🤖 Geminiで解析中... (数秒かかります)", end="\r")
            text = extract_text_with_gemini(img)
            
            if text and not text.startswith("[Gemini API Error]"):
                pages.append(text)
                print(f"  ✅ 完了 ({len(text)}文字)                 ")
                print(f"  プレビュー: {text[:40].replace(chr(10), ' ')}...")
            else:
                print(f"  ⚠️ 読み取り失敗: {text}               ")
        
    input("\n終了するにはEnterを押してください...")

if __name__ == "__main__":
    main()
