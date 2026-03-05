---
name: remotion-best-practices
description: Best practices for Remotion - Video creation in React
metadata:
  tags: remotion, video, react, animation, composition
---

## When to use

Use this skills whenever you are dealing with Remotion code to obtain the domain-specific knowledge.

## Captions

When dealing with captions or subtitles, load the [./rules/subtitles.md](./rules/subtitles.md) file for more information.

## Using FFmpeg

For some video operations, such as trimming videos or detecting silence, FFmpeg should be used. Load the [./rules/ffmpeg.md](./rules/ffmpeg.md) file for more information.

## Audio visualization

When needing to visualize audio (spectrum bars, waveforms, bass-reactive effects), load the [./rules/audio-visualization.md](./rules/audio-visualization.md) file for more information.

## How to use

Read individual rule files for detailed explanations and code examples:

### Media & Assets
- [rules/assets.md](rules/assets.md) - Importing images, videos, audio, and fonts
- [rules/images.md](rules/images.md) / [rules/videos.md](rules/videos.md) / [rules/audio.md](rules/audio.md) - Embedding media
- [rules/fonts.md](rules/fonts.md) - Typescaling and custom fonts
- [rules/gifs.md](rules/gifs.md) / [rules/lottie.md](rules/lottie.md) - Animations

### Measurement & Layout
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) / [rules/measuring-text.md](rules/measuring-text.md) - Sizing and layout restrictions

### Animation & Timing
- [rules/animations.md](rules/animations.md) / [rules/text-animations.md](rules/text-animations.md) / [rules/timing.md](rules/timing.md) - Animation patterns and curves
- [rules/transitions.md](rules/transitions.md) / [rules/sequencing.md](rules/sequencing.md) - Flow control and sequencing
- [rules/trimming.md](rules/trimming.md) - Cutting scenes

### Core & Configuration
- [rules/compositions.md](rules/compositions.md) - Structure and props
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Dynamic lengths and props
- [rules/parameters.md](rules/parameters.md) - Zod schemas
- [rules/tailwind.md](rules/tailwind.md) - Styling integration

### Advanced & Integrations
- [rules/3d.md](rules/3d.md) - React Three Fiber context
- [rules/charts.md](rules/charts.md) - Data visualization patterns
- [rules/maps.md](rules/maps.md) - Mapbox maps
- [rules/voiceover.md](rules/voiceover.md) - ElevenLabs TTS integration
- [rules/light-leaks.md](rules/light-leaks.md) - Visual FX
- [rules/transparent-videos.md](rules/transparent-videos.md) - Alpha channel rendering
- **Mediabunny Tools**: [rules/can-decode.md](rules/can-decode.md) / [rules/extract-frames.md](rules/extract-frames.md) / [rules/get-audio-duration.md](rules/get-audio-duration.md) / [rules/get-video-dimensions.md](rules/get-video-dimensions.md) / [rules/get-video-duration.md](rules/get-video-duration.md)
