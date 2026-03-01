#!/usr/bin/env python3
"""
AI Image Generator — Antigravity 特典スキル（Standard版）
画像生成スクリプト（1ファイル完結・従量課金）

使い方:
  python generate_image.py --prompt "プロンプト" --output "output.png"
  python generate_image.py --help

必要なもの:
  - pip install google-genai Pillow
  - 環境変数 GOOGLE_API_KEY にAPIキーを設定
"""

import argparse
import os
import sys
import io
import base64
import traceback

# === UTF-8 強制（Windows文字化け対策） ===
try:
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# =============================================================================
# エラーメッセージ（日本語）
# =============================================================================
ERRORS = {
    "no_api_key": """
❌ APIキーが設定されていません。

以下のいずれかの方法で設定してください:

【方法1】環境変数に設定（推奨）
  Windows (PowerShell):
    $env:GOOGLE_API_KEY = "あなたのAPIキー"

  Mac/Linux:
    export GOOGLE_API_KEY="あなたのAPIキー"

【方法2】コマンドラインで指定
  python generate_image.py --api_key "あなたのAPIキー" --prompt "..." --output "..."

APIキーの取得方法:
  1. https://aistudio.google.com/apikey を開く
  2. 「APIキーを作成」をクリック
  3. 表示されたキーをコピー
""",
    "no_sdk": """
❌ google-genai パッケージがインストールされていません。

以下のコマンドでインストールしてください:
  pip install google-genai
""",
    "no_pillow": """
❌ Pillow パッケージがインストールされていません。

以下のコマンドでインストールしてください:
  pip install Pillow
""",
    "api_error": """
❌ 画像生成中にエラーが発生しました。

考えられる原因:
  1. APIキーが無効 → https://aistudio.google.com/apikey で確認
  2. ネットワーク接続の問題 → インターネット接続を確認
  3. APIの一時的な負荷 → 数分待ってから再試行

エラー詳細: {error}
""",
    "no_image_in_response": """
⚠️ AIがテキストで応答しました（画像が生成されませんでした）。

プロンプトを調整してみてください:
  - より具体的な描写にする
  - 「illustration of」や「photo of」を先頭に追加する
  - 不適切なコンテンツと判定された可能性がある場合は表現を変える

AIの応答: {text}
""",
}


# =============================================================================
# SDK読み込み（エラー時に日本語ガイド）
# =============================================================================
try:
    from google import genai
    from google.genai import types
except ImportError:
    print(ERRORS["no_sdk"])
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print(ERRORS["no_pillow"])
    sys.exit(1)


# =============================================================================
# 画像生成コア
# =============================================================================
def generate_image(
    api_key: str,
    prompt: str,
    output_path: str,
    model: str = "gemini-3-pro-image-preview",
    aspect_ratio: str = "16:9",
    ref_image_path: str = None,
) -> str:
    """
    Nano Banana Pro で画像を生成して保存する。

    Returns:
        保存先のパス（成功時）、None（失敗時）
    """
    # クライアント初期化
    client = genai.Client(api_key=api_key)

    # コンテンツ構築
    contents = []

    # 参照画像がある場合
    if ref_image_path and os.path.exists(ref_image_path):
        print(f"📎 参照画像を読み込み中: {os.path.basename(ref_image_path)}")
        try:
            ref_img = Image.open(ref_image_path)
            contents.append(ref_img)
        except Exception as e:
            print(f"⚠️ 参照画像の読み込みに失敗しました: {e}")
            print("   参照画像なしで生成を続行します。")

    # プロンプト追加
    contents.append(prompt)

    # 生成設定
    config_params = {
        "response_modalities": ["IMAGE"],
        "image_config": types.ImageConfig(aspect_ratio=aspect_ratio),
    }

    print(f"🎨 画像を生成中...")
    print(f"   モデル: {model}")
    print(f"   サイズ: {aspect_ratio}")
    print(f"   プロンプト: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")

    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=types.GenerateContentConfig(**config_params),
        )
    except Exception as e:
        print(ERRORS["api_error"].format(error=str(e)))
        return None

    # レスポンス解析
    if not response.candidates:
        print("❌ 応答が空でした。プロンプトを変えて再試行してください。")
        return None

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            # 画像データを保存
            output_dir = os.path.dirname(os.path.abspath(output_path))
            os.makedirs(output_dir, exist_ok=True)

            image_data = part.inline_data.data
            with open(output_path, "wb") as f:
                f.write(image_data)

            file_size = os.path.getsize(output_path)
            size_str = (
                f"{file_size / 1024:.0f}KB"
                if file_size < 1024 * 1024
                else f"{file_size / 1024 / 1024:.1f}MB"
            )
            print(f"\n✅ 画像を保存しました！")
            print(f"   📁 保存先: {output_path}")
            print(f"   📏 サイズ: {size_str}")
            return output_path

        elif part.text:
            print(ERRORS["no_image_in_response"].format(text=part.text[:200]))
            return None

    print("❌ 応答に画像データが含まれていませんでした。")
    return None


# =============================================================================
# メイン
# =============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="AI Image Generator — Antigravity 特典スキル（Standard版）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # YouTubeサムネイル（16:9, デフォルト）
  python generate_image.py --prompt "サイバーパンクな街並み、ネオンライト" --output thumbnail.png

  # Xポスト用の正方形画像
  python generate_image.py --prompt "かわいい猫のイラスト" --output post.png --aspect_ratio 1:1

  # 参照画像付きで生成
  python generate_image.py --prompt "同じキャラクターが海辺にいる" --output beach.png --ref_image character.png

  # ストーリー形式の縦長画像
  python generate_image.py --prompt "魔法の森の入口" --output story.png --aspect_ratio 9:16

対応アスペクト比:
  16:9  — YouTubeサムネ、Xカード、Noteバナー（デフォルト）
  1:1   — Xポスト正方形、プロフィール画像
  9:16  — スマホ壁紙、ストーリー
  3:4   — ポートレート
  4:3   — プレゼン資料

コスト目安（公式料金: ai.google.dev/pricing）:
  Nano Banana Pro 2K: 約¥20/枚 | 4K: 約¥36/枚
  Nano Banana 1K:     約¥6/枚
  ※使った分だけの従量課金。APIキー発行は無料
        """,
    )

    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="画像生成のプロンプト（日本語・英語どちらもOK）",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="保存先ファイルパス（例: output.png）",
    )
    parser.add_argument(
        "--aspect_ratio",
        type=str,
        default="16:9",
        choices=["16:9", "1:1", "9:16", "3:4", "4:3"],
        help="アスペクト比（デフォルト: 16:9）",
    )
    parser.add_argument(
        "--ref_image",
        type=str,
        default=None,
        help="参照画像のパス（キャラクター一貫性に便利）",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gemini-3-pro-image-preview",
        help="使用するモデル（デフォルト: Nano Banana Pro）",
    )
    parser.add_argument(
        "--api_key",
        type=str,
        default=None,
        help="Google API キー（環境変数 GOOGLE_API_KEY の代わりに指定）",
    )

    args = parser.parse_args()

    # APIキー取得
    api_key = args.api_key or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print(ERRORS["no_api_key"])
        sys.exit(1)

    # 生成実行
    result = generate_image(
        api_key=api_key,
        prompt=args.prompt,
        output_path=args.output,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        ref_image_path=args.ref_image,
    )

    if not result:
        sys.exit(1)


if __name__ == "__main__":
    main()
