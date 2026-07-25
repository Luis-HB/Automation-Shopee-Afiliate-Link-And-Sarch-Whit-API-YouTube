from dataclasses import dataclass, field


@dataclass
class VideoResult:

    provider: str

    video_id: str

    titulo: str

    url: str

    thumbnail: str = ""

    canal: str = ""

    views: int = 0

    likes: int = 0

    duracao: int = 0

    score: float = 0

    metadata: dict = field(default_factory=dict)