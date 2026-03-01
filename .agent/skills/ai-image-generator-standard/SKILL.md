---
name: ai-image-generator-standard
description: >
  Generates images using Google Gemini (Nano Banana Pro) with pay-as-you-go
  API billing. Handles initial setup with cost-first explanation, API key
  configuration, and image generation with YouTube thumbnail (16:9) as default.
  Use when the user wants to generate images, create thumbnails, banners,
  illustrations, or needs help setting up image generation with a Google API key.
---

# AI Image Generator — Standard版（全購入者向け特典スキル）

Google AI の画像生成モデル **Nano Banana Pro** を使って、
高品質な画像を生成するスキルです。

> 💰 料金: 1枚あたり約¥20（2K解像度）。使った分だけの従量課金。

## When to use this skill（使いどころ）
- **画像を作りたい時**: 「YouTubeサムネ作って」「Xポスト用の画像を生成して」等
- **セットアップしたい時**: 「画像生成のセットアップをして」「APIキーの設定を教えて」等
- **プロンプトを相談したい時**: 「プロンプトのコツを教えて」「どう書けばいい？」等
- **料金を知りたい時**: 「画像生成っていくらかかるの？」等

## Workflow

### 1. Usage Check
- **Crucial**: スクリプトを使う前に必ず `--help` で引数を確認:
  ```
  python scripts/generate_image.py --help
  python scripts/setup_check.py --help
  ```

### 2. モード判定
ユーザーの発言から以下の4モードを判定する:

| モード | 判定キーワード | 実行内容 |
|:---|:---|:---|
| 💰 料金確認 | 料金, いくら, コスト, 値段, 費用 | → Step 3a |
| 🚀 セットアップ | セットアップ, 設定, APIキー, 初期設定 | → Step 3b |
| 🎨 画像生成 | 画像, サムネ, バナー, イラスト, 生成 | → Step 3c |
| 📖 プロンプト相談 | プロンプト, コツ, どう書く, テンプレ | → Step 3d |

### 3a. 料金確認モード
`resources/setup_guide.md` の Step 1（料金を知る）を読み込み、以下を伝える:
- 1枚あたりの料金（NB Pro 2K: ¥20 / 4K: ¥36 / NB: ¥6）
- 月額試算テーブル
- 無料: APIキー発行自体は無料。使った分だけ課金

### 3b. セットアップモード
1. **まず料金を説明する（必須）** → `resources/setup_guide.md` の Step 1
2. 料金に納得したら → Step 2〜4 を順番に案内
3. `python scripts/setup_check.py --check` で診断
4. 全チェックPASSしたら「準備完了！画像を作りましょう」と案内

### 3c. 画像生成モード
1. **初回利用確認**: ユーザーに「セットアップは完了していますか？」と確認
   - 未完了なら → セットアップモードへ誘導
2. ユーザーのリクエストからプロンプトを構築
   - 日本語リクエストの場合: エージェントが英語プロンプトに変換して提案
   - `resources/prompting_tips.md` のテンプレートを参考にする
3. 出力先パスを決定
4. 実行:
   ```
   python scripts/generate_image.py \
     --prompt "構築したプロンプト" \
     --output "出力パス.png" \
     --aspect_ratio "16:9"
   ```
5. 生成結果と費用（約¥20/枚）をユーザーに報告

**デフォルト設定**:
- モデル: `gemini-3-pro-image-preview`（Nano Banana Pro）
- アスペクト比: `16:9`（YouTubeサムネサイズ）
- 出力形式: PNG

**対応アスペクト比**:
| 比率 | 用途 |
|:---|:---|
| 16:9 | YouTubeサムネ / Xカード / Noteバナー |
| 1:1 | Xポスト正方形 / プロフィール |
| 9:16 | スマホ壁紙 / ストーリー |
| 3:4 | ポートレート |
| 4:3 | プレゼン資料 |

### 3d. プロンプト相談モード
1. `resources/prompting_tips.md` を読み込む
2. ユーザーの目的に合ったテンプレートを提案

## Usage Instructions

### Execution Steps (Agent)
1. **Preparation**: モードを判定
2. **Execution**: スクリプト実行時は UTF-8 強制:
   ```
   [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $env:PYTHONUTF8=1; python scripts/generate_image.py ...
   ```
3. **Report**: 生成結果のパス、画像、費用をユーザーに表示

## Tips
- **コスト**: NB Pro 2K = 約¥20/枚。月10枚で約¥200。月50枚で約¥1,000
- **日本語テキスト**: Nano Banana Pro は日本語テキストの描画が得意。ただし10文字以上は崩れやすい
- **参照画像**: `--ref_image` を使えばキャラクターの一貫性を保てる
