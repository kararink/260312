---
name: agents
description: Build voice AI agents with ElevenLabs. Use when creating voice assistants, customer service bots, interactive voice characters, or any real-time voice conversation experience.
license: MIT
compatibility: Requires internet access and an ElevenLabs API key (ELEVENLABS_API_KEY).
metadata: {"openclaw": {"requires": {"env": ["ELEVENLABS_API_KEY"]}, "primaryEnv": "ELEVENLABS_API_KEY"}}
---

# ElevenLabs Agents Platform

Build voice AI agents with natural conversations, multiple LLM providers, custom tools, and easy web embedding.

## Quick Start (CLI)

The ElevenLabs CLI is the recommended way to create and manage agents:

```bash
# Install CLI and authenticate
npm install -g @elevenlabs/cli
elevenlabs auth login

# Initialize project and create an agent
elevenlabs agents init
elevenlabs agents add "My Assistant" --template default

# Push to ElevenLabs platform
elevenlabs agents push
```

**Available templates:** `default`, `minimal`, `voice-only`, `text-only`, `customer-service`, `assistant`

## Managing Agents (CLI)

```bash
# List agents and check status
elevenlabs agents list
elevenlabs agents status

# Import agents from platform to local config
elevenlabs agents pull                      # Import all agents
elevenlabs agents pull --agent <agent-id>   # Import specific agent

# Push local changes to platform
elevenlabs agents push              # Upload configurations
elevenlabs agents push --dry-run    # Preview changes first

# Add tools to agents
elevenlabs agents tools add "Weather API" --type webhook --config-path ./weather.json
```

## Configuration

| Provider | Models |
|----------|--------|
| OpenAI | `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo` |
| Anthropic | `claude-3-5-sonnet`, `claude-3-5-haiku` |
| Google | `gemini-1.5-pro`, `gemini-1.5-flash` |
| Custom | `custom-llm` (bring your own endpoint) |

**Popular voices:** `JBFqnCBsd6RMkjVDRZzb` (George), `EXAVITQu4vr4xnSDxMaL` (Sarah), `onwK4e9ZLuTAKqWW03F9` (Daniel), `XB0fDUnXU5powFXDhCwa` (Charlotte)

**Turn-taking modes:** `server_vad` (auto-detect speech end) or `turn_based` (explicit signals)

## References

- [API Examples (Python, JS, cURL)](references/api_examples.md) - SDK setup, Creating Agents, Starting Conversations, Tools, Outbound Calls, Error Handling
- [Installation Guide](references/installation.md) - SDK setup and migration
- [Agent Configuration](references/agent-configuration.md) - All config options and CRUD examples
- [Client Tools](references/client-tools.md) - Webhook, client, and system tools
- [Widget Embedding](references/widget-embedding.md) - Website integration
- [Outbound Calls](references/outbound-calls.md) - Twilio phone call integration
