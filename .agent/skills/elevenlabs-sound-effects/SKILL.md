---
name: sound-effects
description: Generate sound effects from text descriptions using ElevenLabs. Use when creating sound effects, generating audio textures, producing ambient sounds, cinematic impacts, UI sounds, or any audio that isn't speech. Supports looping, duration control, and prompt influence tuning.
license: MIT
compatibility: Requires internet access and an ElevenLabs API key (ELEVENLABS_API_KEY).
metadata: {"openclaw": {"requires": {"env": ["ELEVENLABS_API_KEY"]}, "primaryEnv": "ELEVENLABS_API_KEY"}}
---

# ElevenLabs Sound Effects

Generate sound effects from text descriptions — supports looping, custom duration, and prompt adherence control.

## Overview

Convert simple text descriptions into high-quality sound effects, ambient atmospheres, and audio textures. The v2 model offers more control over prompt adherence, generation duration, and seamless looping for long-running ambient sounds.

## Capabilities

- **Sound Generation:** Create almost any sound effect strictly from a text prompt.
- **Custom Durations:** Request exactly the length of audio you need (0.5 up to 30 seconds).
- **Prompt Adherence:** Tweak how strongly the engine should try to match your prompt compared to audio diversity.
- **Looping:** Specifying "loop=true" generates sound effects explicitly intended to be tiled/looped seamlessly forever.

## Prompt Tips Example

You can achieve better sounds by describing the exact texture, action, background, or mood:
- *Atmosphere:* "Eerie wind howling through an abandoned building"
- *Action:* "Layered heavy armor footsteps walking carefully through gravel"
- *Impact:* "Cinematic braam impact with metallic screech"

## References

- [API Examples (Python, JS, cURL) & Features](references/api_examples.md) - Contains quick start snippets, parameter definitions, prompt tips, and lists of valid output formats like MP3, OPUS, and PCM.
- [Installation Guide](references/installation.md)
