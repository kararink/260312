# AI Image Generator Workflow Details

## 3a. 料金確認モード
`resources/setup_guide.md` の Step 1（料金を知る）を読み込み、以下を伝える:
- 1枚あたりの料金（NB Pro 2K: ¥20 / 4K: ¥36 / NB: ¥6）
- 月額試算テーブル
- 無料: APIキー発行自体は無料。使った分だけ課金

## 3b. セットアップモード
1. **まず料金を説明する（必須）** → `resources/setup_guide.md` の Step 1
2. 料金に納得したら → Step 2〜4 を順番に案内
3. `python scripts/setup_check.py --check` で診断
4. 全チェックPASSしたら「準備完了！画像を作りましょう」と案内

## 3c. 画像生成モード
1. **初回利用確認**: ユーザーに「セットアップは完了していますか？」と確認
   - 未完了なら → セットアップモードへ誘導
2. ユーザーのリクエストからプロンプトを構築
   - 日本語リクエストの場合: エージェントが英語プロンプトに変換して提案
   - `resources/prompting_tips.md` のテンプレートを参考にする
3. 出力先パスを決定
4. 実行:
   ```bash
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

## 3d. プロンプト相談モード
1. `resources/prompting_tips.md` を読み込む
2. ユーザーの目的に合ったテンプレートを提案

## Execution Steps Tips (Agent)
1. **Preparation**: モードを判定
2. **Execution**: スクリプト実行時は UTF-8 強制:
   ```powershell
   [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $env:PYTHONUTF8=1; python scripts/generate_image.py ...
   ```
3. **Report**: 生成結果のパス、画像、費用をユーザーに表示
