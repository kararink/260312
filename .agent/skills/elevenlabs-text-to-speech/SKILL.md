---
name: text-to-speech
description: Convert text to speech using ElevenLabs voice AI. Use when generating audio from text, creating voiceovers, building voice apps, or synthesizing speech in 70+ languages.
license: MIT
compatibility: Requires internet access and an ElevenLabs API key (ELEVENLABS_API_KEY).
metadata: {"openclaw": {"requires": {"env": ["ELEVENLABS_API_KEY"]}, "primaryEnv": "ELEVENLABS_API_KEY"}}
---

# ElevenLabs Text-to-Speech

Generate natural speech from text - supports 74+ languages, multiple models for quality vs latency tradeoffs.

## Overview

Convert provided text into high-quality spoken audio. You can choose from a variety of voices, control pronunciation, and adjust voice stability/similarity to fit your exact use case.

## Models

| Model ID | Languages | Latency | Best For |
|----------|-----------|---------|----------|
| `eleven_v3` | 74 | Standard | Highest quality, emotional range |
| `eleven_multilingual_v2` | 29 | Standard | High quality, most use cases |
| `eleven_flash_v2_5` | 32 | ~75ms | Ultra-low latency, real-time |
| `eleven_flash_v2` | English | ~75ms | English-only, fastest |
| `eleven_turbo_v2_5` | 32 | Low | Balanced quality/speed |

## Voice IDs

Use pre-made voices or create custom voices in the dashboard.

**Popular voices:**
- `JBFqnCBsd6RMkjVDRZzb` - George (male, narrative)
- `EXAVITQu4vr4xnSDxMaL` - Sarah (female, soft)
- `onwK4e9ZLuTAKqWW03F9` - Daniel (male, authoritative)
- `XB0fDUnXU5powFXDhCwa` - Charlotte (female, conversational)

You can list all available voices using the SDK: `client.voices.get_all()`

## Output Formats

| Format | Description |
|--------|-------------|
| `mp3_44100_128` | MP3 44.1kHz 128kbps (default) - compressed, good for web/apps |
| `mp3_44100_192` | MP3 44.1kHz 192kbps (Creator+) - higher quality compressed |
| `pcm_16000` | Raw uncompressed audio at 16kHz - use for real-time processing |
| `pcm_22050` | Raw uncompressed audio at 22.05kHz |
| `pcm_24000` | Raw uncompressed audio at 24kHz - good balance for streaming |
| `pcm_44100` | Raw uncompressed audio at 44.1kHz (Pro+) - CD quality |
| `ulaw_8000` | μ-law compressed 8kHz - standard for phone systems (Twilio, telephony) |

## References

- [API Examples (Python, JS, cURL) & Features](references/api_examples.md) - Contains usage for generating speech, configuring Voice Settings, Language Enforcement, Text Normalization, Request Stitching, Tracking Costs, and Streaming.
- [Installation Guide](references/installation.md)
- [Streaming Audio](references/streaming.md)
- [Voice Settings Details](references/voice-settings.md)
