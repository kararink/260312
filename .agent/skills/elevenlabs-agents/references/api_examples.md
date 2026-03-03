# ElevenLabs Agents API Examples

## Quick Start (SDK & cURL)

### Python

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs()

agent = client.conversational_ai.agents.create(
    name="My Assistant",
    conversation_config={
        "agent": {"first_message": "Hello! How can I help?", "language": "en"},
        "tts": {"voice_id": "JBFqnCBsd6RMkjVDRZzb"}
    },
    prompt={
        "prompt": "You are a helpful assistant. Be concise and friendly.",
        "llm": "gpt-4o-mini",
        "temperature": 0.7
    }
)
```

### JavaScript

```javascript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
const client = new ElevenLabsClient();

const agent = await client.conversationalAi.agents.create({
  name: "My Assistant",
  conversationConfig: {
    agent: { firstMessage: "Hello! How can I help?", language: "en" },
    tts: { voiceId: "JBFqnCBsd6RMkjVDRZzb" }
  },
  prompt: { prompt: "You are a helpful assistant.", llm: "gpt-4o-mini", temperature: 0.7 }
});
```

### cURL

```bash
curl -X POST "https://api.elevenlabs.io/v1/convai/agents/create" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"name": "My Assistant", "conversation_config": {"agent": {"first_message": "Hello!", "language": "en"}, "tts": {"voice_id": "JBFqnCBsd6RMkjVDRZzb"}}, "prompt": {"prompt": "You are helpful.", "llm": "gpt-4o-mini"}}'
```

## Starting Conversations

**Server-side (Python):** Get signed URL for client connection:
```python
signed_url = client.conversational_ai.conversations.get_signed_url(agent_id="your-agent-id")
```

**Client-side (JavaScript):**
```javascript
import { Conversation } from "@elevenlabs/client";

const conversation = await Conversation.startSession({
  agentId: "your-agent-id",
  onMessage: (msg) => console.log("Agent:", msg.message),
  onUserTranscript: (t) => console.log("User:", t.message),
  onError: (e) => console.error(e)
});
```

**React Hook:**
```typescript
import { useConversation } from "@elevenlabs/react";

const conversation = useConversation({ onMessage: (msg) => console.log(msg) });
// Get signed URL from backend, then:
await conversation.startSession({ signedUrl: token });
```

## Tools Definition Example

Extend agents with webhook, client, or system tools:

```python
tools=[
    # Webhook: server-side API call
    {"type": "webhook", "name": "get_weather", "description": "Get weather",
     "webhook": {"url": "https://api.example.com/weather", "method": "POST"},
     "parameters": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}},
    # System: built-in capabilities
    {"type": "system", "name": "end_call"},
    {"type": "system", "name": "transfer_to_number", "phone_number": "+1234567890"}
]
```

**Client tools** run in browser:
```javascript
clientTools: {
  show_product: async ({ productId }) => {
    document.getElementById("product").src = `/products/${productId}`;
    return { success: true };
  }
}
```

## Outbound Calls

Make outbound phone calls using your agent via Twilio integration:

### Python
```python
response = client.conversational_ai.twilio.outbound_call(
    agent_id="your-agent-id",
    agent_phone_number_id="your-phone-number-id",
    to_number="+1234567890"
)
print(f"Call initiated: {response.conversation_id}")
```

### JavaScript
```javascript
const response = await client.conversationalAi.twilio.outboundCall({
  agentId: "your-agent-id",
  agentPhoneNumberId: "your-phone-number-id",
  toNumber: "+1234567890",
});
```

### cURL
```bash
curl -X POST "https://api.elevenlabs.io/v1/convai/twilio/outbound-call" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"agent_id": "your-agent-id", "agent_phone_number_id": "your-phone-number-id", "to_number": "+1234567890"}'
```

## Managing Agents (SDK Examples)

```python
# List
agents = client.conversational_ai.agents.list()

# Get
agent = client.conversational_ai.agents.get(agent_id="your-agent-id")

# Update (partial - only include fields to change)
client.conversational_ai.agents.update(agent_id="your-agent-id", name="New Name")
client.conversational_ai.agents.update(agent_id="your-agent-id",
    prompt={"prompt": "New instructions", "llm": "claude-3-5-sonnet"})

# Delete
client.conversational_ai.agents.delete(agent_id="your-agent-id")
```

## Error Handling

```python
try:
    agent = client.conversational_ai.agents.create(...)
except Exception as e:
    print(f"API error: {e}")
```

Common errors: **401** (invalid key), **404** (not found), **422** (invalid config), **429** (rate limit)
