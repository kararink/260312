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

## Models

| Model ID | Description | Best For |
|----------|-------------|----------|
| `scribe_v2` | State-of-the-art accuracy, 90+ languages | Batch transcription, subtitles, long-form audio |
| `scribe_v2_realtime` | Low latency (~150ms) | Live transcription, voice agents |

## Supported Formats

**Audio:** MP3, WAV, M4A, FLAC, OGG, WebM, AAC, AIFF, Opus
**Video:** MP4, AVI, MKV, MOV, WMV, FLV, WebM, MPEG, 3GPP

**Limits:** Up to 3GB file size, 10 hours duration

## Features Available

- **Transcription with Timestamps:** Get precise start and end times for every word.
- **Speaker Diarization:** Identify which speaker is talking for each word.
- **Keyterm Prompting:** Provide specific words or jargon to improve recognition.
- **Language Detection:** Automatically detect the spoken language.
- **Real-Time Streaming:** Transcribe live audio with ultra-low latency.

## References

- [API Examples (Python, JS, cURL) & Features](references/api_examples.md) - Contains code snippets for SDK usage, timestamps, diarization, real-time streaming, and JSON response formats.
- [Installation Guide](references/installation.md)
- [Transcription Options](references/transcription-options.md)
- [Real-Time Client-Side Streaming](references/realtime-client-side.md)
- [Real-Time Server-Side Streaming](references/realtime-server-side.md)
- [Commit Strategies](references/realtime-commit-strategies.md)
- [Real-Time Event Reference](references/realtime-events.md)
