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

## Features

- **Models**: Choose between `eleven_v3` (Highest quality), `eleven_multilingual_v2` (Most use cases), and `eleven_flash_v2_5` (Ultra-low latency, real-time).
- **Voice IDs**: Use pre-made voices or create custom ones.
- **Output Formats**: Supports MP3, PCM, and μ-law.

## References

- [API Examples (Python, JS, cURL) & Features](references/api_examples.md) - Contains usage for generating speech, configuring Voice Settings, Language Enforcement, Text Normalization, Request Stitching, Tracking Costs, and Streaming.
- [Installation Guide](references/installation.md)
- [Streaming Audio](references/streaming.md)
- [Voice Settings Details](references/voice-settings.md)
