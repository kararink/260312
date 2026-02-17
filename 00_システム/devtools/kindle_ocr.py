#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kindle OCR Tool (High Precision Edition)
著作権法第30条に基づく私的使用目的の複製ツール
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import pyautogui
    from PIL import Image, ImageOps, ImageEnhance
    import pytesseract
    import win32gui
    import win32con
    HAS_WIN32 = True
except ImportError as e:
    print(f"エラー: 必要なライブラリが見つかりません: {e}")
    print("setup_kindle_ocr.bat を実行してください。")
    input("Enterキーで終了...")
    sys.exit(1)

# Tesseractパス設定
TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    os.path.join(os.getenv('LOCALAPPDATA', ''), r'Programs\Tesseract-OCR\tesseract.exe'),
]

def find_tesseract():
    for path in TESSERACT_PATHS:
        if os.path.exists(path):
            return path
    return None

def setup_tesseract():
    path = find_tesseract()
    if not path:
        print("エラー: Tesseract OCRが見つかりません。")
        print("https://github.com/UB-Mannheim/tesseract/wiki からインストールしてください。")
        return False
    pytesseract.pytesseract.tesseract_cmd = path
    return True

def preprocess_image(image):
    """OCR精度向上のための画像前処理"""
    # 1. グレースケール変換
    img = ImageOps.grayscale(image)
    
    # 2. 画像を2倍に拡大（小さい文字の認識率向上）
    width, height = img.size
    img = img.resize((width * 2, height * 2), Image.Resampling.LANCZOS)
    
    # 3. コントラストを強調
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    
    # 4. 二値化（しきい値処理）- 文字をくっきりさせる
    # img = img.point(lambda x: 0 if x < 140 else 255) 
    # ※背景色によっては逆効果になることがあるので、一旦コントラスト強調までにする
    
    return img

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

def extract_text(image):
    """日本語OCR実行"""
    # 読み取り精度重視の設定
    # --oem 3: Default OCR Engine
    # --psm 6: Assume a single uniform block of text
    config = r'--oem 3 --psm 6'
    try:
        return pytesseract.image_to_string(image, lang='jpn', config=config).strip()
    except:
        # 日本語だけだと失敗する場合、英語混じりで再トライ
        try:
            return pytesseract.image_to_string(image, lang='jpn+eng', config=config).strip()
        except Exception as e:
            return f"[OCR Error] {e}"

def main():
    if not setup_tesseract():
        input("Enterキーで終了...")
        return

    print("="*60)
    print("  Kindle OCR Tool - High Precision Mode")
    print("="*60)
    print("  画像の拡大・補正処理を追加しました。")
    print("  より高精度に文字を認識します。")
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
            
            print("  ⚙️ 画像補正中...  ", end="\r")
            processed_img = preprocess_image(img)
            
            # デバッグ用に画像保存（オプション）
            # processed_img.save("debug_last_capture.png")
            
            print("  📝 文字読取中...  ", end="\r")
            text = extract_text(processed_img)
            
            if text:
                pages.append(text)
                print(f"  ✅ 完了 ({len(text)}文字)")
                print(f"  プレビュー: {text[:40].replace(chr(10), ' ')}...")
            else:
                print("  ⚠️ 文字を読み取れませんでした")
        
    input("\n終了するにはEnterを押してください...")

if __name__ == "__main__":
    main()
