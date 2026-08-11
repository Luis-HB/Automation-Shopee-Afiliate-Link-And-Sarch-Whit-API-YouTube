from dataclasses import dataclass, field


@dataclass
class Evidence:

    queries: list = field(default_factory=list)

    videos: list = field(default_factory=list)