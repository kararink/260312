---
name: music
description: Generate music using ElevenLabs Music API. Use when creating instrumental tracks, songs with lyrics, background music, jingles, or any AI-generated music composition. Supports prompt-based generation, composition plans for granular control, and detailed output with metadata.
license: MIT
compatibility: Requires internet access and an ElevenLabs API key (ELEVENLABS_API_KEY).
metadata: {"openclaw": {"requires": {"env": ["ELEVENLABS_API_KEY"]}, "primaryEnv": "ELEVENLABS_API_KEY"}}
---

# ElevenLabs Music Generation

Generate music from text prompts - supports instrumental tracks, songs with lyrics, and fine-grained control via composition plans.

## Overview

Create original music using prompt-based generation. Whether you need an instrumental background score, a catchy jingle, or a full song with lyrics, the Music API provides various modes of composition—from one-shot generation to detailed multi-step composition plans for granular control over styles, sections, and mood.

## Features

- **Composition Plans**: For granular control, generate a plan before committing to audio synthesis to inspect and modify styles.
- **Content Limitations**: Cannot reference specific artists, bands, or copyrighted lyrics. See references for handling generation errors.

## References

- [API Examples (Python, JS, cURL) & Features](references/api_examples.md) - Contains code snippets for quickly generating music tracks, fetching and editing composition plans, and handling common API endpoints.
- [Installation Guide](references/installation.md)
- [API Reference](references/api_reference.md)
