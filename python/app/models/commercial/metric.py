from dataclasses import dataclass
from typing import Any


@dataclass
class Metric:

    level: str

    value: Any

    description: str = ""