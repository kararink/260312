#!/usr/bin/env python3
"""
AI Image Generator — セットアップ診断（Standard版）
環境・API の状態を一括チェックします。

使い方:
  python setup_check.py --check
"""

import os
import sys
import io

# === UTF-8 強制 ===
try:
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def print_header():
    print("=" * 56)
    print("  🔍 AI Image Generator セットアップ診断")
    print("=" * 56)
    print()


def check_sdk():
    """google-genai SDKの確認"""
    try:
        from google import genai
        version = getattr(genai, '__version__', '不明')
        print(f"  [✅] google-genai SDK      : インストール済み (v{version})")
        return True
    except ImportError:
        print(f"  [❌] google-genai SDK      : 未インストール")
        print(f"       → 修正: pip install google-genai")
        return False


def check_pillow():
    """Pillowの確認"""
    try:
        from PIL import Image
        import PIL
        version = getattr(PIL, '__version__', '不明')
        print(f"  [✅] Pillow                : インストール済み (v{version})")
        return True
    except ImportError:
        print(f"  [❌] Pillow                : 未インストール")
        print(f"       → 修正: pip install Pillow")
        return False


def check_api_key():
    """GOOGLE_API_KEY環境変数の確認"""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        masked = api_key[:4] + "..." + api_key[-3:] if len(api_key) > 10 else "***"
        print(f"  [✅] GOOGLE_API_KEY        : 設定済み ({masked})")
        return api_key
    else:
        print(f"  [❌] GOOGLE_API_KEY        : 未設定")
        print(f"       → 修正:")
        print(f"         Windows(PowerShell): $env:GOOGLE_API_KEY = \"あなたのキー\"")
        print(f"         Mac/Linux:           export GOOGLE_API_KEY=\"あなたのキー\"")
        print(f"       → キー取得: https://aistudio.google.com/apikey")
        return None


def check_api_connection(api_key):
    """API接続テスト（軽量テキスト生成）"""
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Reply with only the word 'OK'.",
        )
        if response and response.text:
            print(f"  [✅] API接続テスト         : 成功！")
            return True
        else:
            print(f"  [⚠️] API接続テスト         : 応答は返りましたが内容が空でした")
            return False
    except Exception as e:
        error_msg = str(e)
        print(f"  [❌] API接続テスト         : 失敗")
        if "API_KEY_INVALID" in error_msg or "401" in error_msg:
            print(f"       → APIキーが無効です。正しいキーを設定してください")
            print(f"       → https://aistudio.google.com/apikey で確認")
        elif "RESOURCE_EXHAUSTED" in error_msg or "429" in error_msg:
            print(f"       → APIの利用制限に達しています。数分待ってから再試行してください")
        else:
            print(f"       → エラー: {error_msg[:100]}")
        return False


def check_image_generation(api_key):
    """テスト画像生成"""
    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)

        print(f"  [⏳] テスト画像生成        : 生成中...")

        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents="A simple blue circle on white background",
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio="1:1"),
            ),
        )

        if response.candidates:
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                    test_path = os.path.join(
                        os.path.dirname(os.path.abspath(__file__)),
                        "_test_setup.png"
                    )
                    with open(test_path, "wb") as f:
                        f.write(part.inline_data.data)

                    size_kb = os.path.getsize(test_path) / 1024
                    print(f"\r  [✅] テスト画像生成        : 成功！({size_kb:.0f}KB)")
                    print(f"       → テスト画像: {test_path}")
                    print(f"       💰 このテスト画像の費用: 約¥20")
                    return True

        print(f"\r  [⚠️] テスト画像生成        : 画像が返されませんでした")
        return False

    except Exception as e:
        error_msg = str(e)
        print(f"\r  [❌] テスト画像生成        : 失敗")
        print(f"       → エラー: {error_msg[:150]}")
        return False


def print_cost_info():
    """コスト情報の表示"""
    print()
    print("  " + "─" * 52)
    print("  💰 料金について")
    print("  " + "─" * 52)
    print()
    print("  画像生成は使った分だけ課金されます。")
    print("  APIキーを持っているだけでは料金は発生しません。")
    print()
    print("  ┌──────────────────────┬──────────┐")
    print("  │ モデル                │ 1枚あたり │")
    print("  ├──────────────────────┼──────────┤")
    print("  │ NB Pro  2K(~2048px)  │ 約¥20    │")
    print("  │ NB Pro  4K(~4096px)  │ 約¥36    │")
    print("  │ NB      1K(~1024px)  │ 約¥6     │")
    print("  └──────────────────────┴──────────┘")
    print()
    print("  月10枚(NB Pro 2K): 約¥200 / 月50枚: 約¥1,000")
    print()
    print("  💡 予算が心配な方は、Google Cloud Consoleで")
    print("     予算アラートを設定できます（setup_guide.md 参照）")
    print()


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="AI Image Generator セットアップ診断"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="セットアップ状態をチェック"
    )
    args = parser.parse_args()

    if not args.check:
        parser.print_help()
        return

    print_header()

    results = []

    # 1. SDK チェック
    results.append(("SDK", check_sdk()))

    # 2. Pillow チェック
    results.append(("Pillow", check_pillow()))

    # 3. APIキー チェック
    api_key = check_api_key()
    results.append(("API Key", api_key is not None))

    # 4. API接続テスト
    if api_key:
        results.append(("API Connection", check_api_connection(api_key)))
    else:
        print(f"  [⏭️] API接続テスト         : スキップ（APIキー未設定）")
        results.append(("API Connection", False))

    # 5. テスト画像生成
    if api_key and results[-1][1]:
        results.append(("Image Gen", check_image_generation(api_key)))
    else:
        print(f"  [⏭️] テスト画像生成        : スキップ（前提チェック未通過）")
        results.append(("Image Gen", False))

    # 6. コスト情報
    print_cost_info()

    # サマリー
    print("=" * 56)
    passed = sum(1 for _, ok in results if ok)
    total = len(results)

    if passed == total:
        print(f"  🎉 {passed}/{total} すべてのチェックをパスしました！")
        print(f"     画像生成の準備完了です。")
        print()
        print(f"  次のステップ:")
        print(f"    python generate_image.py \\")
        print(f"      --prompt \"あなたのプロンプト\" \\")
        print(f"      --output \"output.png\"")
    else:
        failed = total - passed
        print(f"  ⚠️ {failed}件のチェックが未通過です。")
        print(f"     上記のガイドに沿って修正してください。")

    print("=" * 56)


if __name__ == "__main__":
    main()
