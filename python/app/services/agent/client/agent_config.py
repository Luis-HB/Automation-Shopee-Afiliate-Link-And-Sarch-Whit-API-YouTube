from dataclasses import dataclass


@dataclass
class AgentConfig:

    webhook_url: str

    timeout: int = 300

    verify_ssl: bool = True

    api_key: str | None = None

    headers: dict | None = None