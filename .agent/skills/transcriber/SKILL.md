---
name: transcriber
description: Transcribes audio files to text using the local Whisper environment.
input:
  audio_path: (required) Absolute path to the audio file to transcribe.
---

# Transcriber Skill

このスキルは、指定された音声ファイルをローカルのWhisperモデルを使用してテキストに変換（文字起こし）します。
既存の `devtools/transcription` 環境（venv）を再利用して実行します。

## Usage

ユーザーが「この音声を文字起こしして」「議事録を作って」等と依頼した場合、または音声ファイルのパスを提示された場合に使用します。

### Command

```bash
c:\Users\杢之助\2nd-Brain\00_システム\devtools\transcription\venv\Scripts\python.exe c:\Users\杢之助\2nd-Brain\.agent\skills\transcriber\scripts\transcribe_target.py "{audio_path}"
```

### Parameters

- `audio_path`: The absolute path to the audio file. Supported formats: .mp3, .wav, .m4a, .mp4, .mpeg, .mpga, .aac, .ogg

### Output behavior

- 文字起こし結果は `c:\Users\杢之助\2nd-Brain\03_知識ベース\00_文字起こしログ` にMarkdownファイルとして保存されます。
- 実行後、生成されたファイルのパスをユーザーに報告してください。
