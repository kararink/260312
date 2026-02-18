---
description: 音声ファイルを文字起こしし、X（Twitter）投稿のドラフトを作成するワークフロー
---

1. **文字起こし (Transcribe)**
   - ユーザーから提供された音声ファイルパスを使用し、`transcriber` スキルを実行してください。
   - コマンド: `c:\Users\杢之助\2nd-Brain\00_システム\devtools\transcription\venv\Scripts\python.exe c:\Users\杢之助\2nd-Brain\.agent\skills\transcriber\scripts\transcribe_target.py "{AudioPath}"`

2. **最新ログの特定 (Identify Log)**
   - 文字起こしが完了したら、`c:\Users\杢之助\2nd-Brain\03_知識ベース\00_文字起こしログ` ディレクトリ内で最も新しい `.md` ファイルを特定し、そのファイルパスを記憶してください。
   - ヒント: `Get-ChildItem` コマンドで `LastWriteTime` でソートすると確実です。

3. **要点抽出 (Extract Insights)**
   - 特定したログファイルの内容を読み込んでください。
   - `.agent/prompts/x_extraction.md` プロンプトを使用して、テキストから「Insight」「Epiphany」「Phrase」を抽出してください。
   - 入力変数: `{{transcript_text}}` = ログファイルの内容

4. **ドラフト作成 (Draft Post)**
   - 抽出された情報を元に、ドラフトを作成してください。
   - `.agent/prompts/x_drafting.md` プロンプトを使用してください。
   - 入力変数: `{{extraction_result}}` = Step 3の出力結果

5. **保存 (Save)**
   - 作成されたドラフトを新しいファイルとして保存してください。
   - 保存先: `c:\Users\杢之助\2nd-Brain\04_Output\01_Drafts`
   - ファイル名規則: `YYYY-MM-DD_X-Draft_{元のファイル名}.md`
   - 保存後、ユーザーにファイルのパスを報告し、レビューを求めてください。
