---
name: speech-to-text
description: Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, or processing spoken content.
license: MIT
compatibility: Requires internet access and an ElevenLabs API key (ELEVENLABS_API_KEY).
metadata: {"openclaw": {"requires": {"env": ["ELEVENLABS_API_KEY"]}, "primaryEnv": "ELEVENLABS_API_KEY"}}
---

# ElevenLabs Speech-to-Text

Transcribe audio to text with Scribe v2 - supports 90+ languages, speaker diarization, and word-level timestamps.

## Overview

Convert audio or video files into accurate text transcripts. The Scribe v2 model provides state-of-the-art accuracy across multiple languages and supports advanced features like identifying different speakers and providing precise timing for every word.

## Features

- **Models**: Includes `scribe_v2` for high accuracy and `scribe_v2_realtime` for low latency (~150ms).
- **Format Support**: Transcribe most audio/video formats (up to 3GB, 10 hours).
- **Advanced Options**: Word-level timestamps, speaker diarization, and language detection.

## References

- [API Examples (Python, JS, cURL) & Features](references/api_examples.md) - Contains code snippets for SDK usage, timestamps, diarization, real-time streaming, and JSON response formats.
- [Installation Guide](references/installation.md)
- [Transcription Options](references/transcription-options.md)
- [Real-Time Client-Side Streaming](references/realtime-client-side.md)
- [Real-Time Server-Side Streaming](references/realtime-server-side.md)
- [Commit Strategies](references/realtime-commit-strategies.md)
- [Real-Time Event Reference](references/realtime-events.md)
