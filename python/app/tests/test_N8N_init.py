from services.agent.client.n8n_client import N8NClient
from services.agent.client.agent_config import AgentConfig
from models.ai_payload import AIPayload
payload = AIPayload()

payload.product = {
    "titulo": "Mouse Gamer Logitech G203",
    "preco": 119.90,
    "nota": 4.9
}

payload.knowledge = {
    "product": {},
    "videos": {},
    "ranking": {},
    "market": {}
}

payload.evidence = {
    "queries": [],
    "videos": []
}

config = AgentConfig(
    webhook_url="http://n8n:5678/webhook-test/commercial-analysis"
)

client = N8NClient(config)

response = client.send(payload)

print(response)