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

## Workflow Overview

### 1. Usage Check
- **Crucial**: スクリプトを使う前に必ず `--help` で引数を確認:
  ```bash
  python scripts/generate_image.py --help
  python scripts/setup_check.py --help
  ```

### 2. モード判定
ユーザーの発言から以下の4モードを判定する:

| モード | 判定キーワード | 実行内容 |
|:---|:---|:---|
| 💰 料金確認 | 料金, いくら, コスト, 値段, 費用 | → `resources/workflow_details.md` の **Step 3a** 参照 |
| 🚀 セットアップ | セットアップ, 設定, APIキー, 初期設定 | → `resources/workflow_details.md` の **Step 3b** 参照 |
| 🎨 画像生成 | 画像, サムネ, バナー, イラスト, 生成 | → `resources/workflow_details.md` の **Step 3c** 参照 |
| 📖 プロンプト相談 | プロンプト, コツ, どう書く, テンプレ | → `resources/workflow_details.md` の **Step 3d** 参照 |

> **Action**: 判定したモードの詳細な実行ステップやパラメータについては、必ず `resources/workflow_details.md` を読み込んでから処理を進めてください。

## Tips
- **コスト**: NB Pro 2K = 約¥20/枚。月10枚で約¥200。月50枚で約¥1,000
- **日本語テキスト**: Nano Banana Pro は日本語テキストの描画が得意。ただし10文字以上は崩れやすい
- **参照画像**: `--ref_image` を使えばキャラクターの一貫性を保てる
