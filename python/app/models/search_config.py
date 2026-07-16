from dataclasses import dataclass, field


@dataclass
class SearchConfig:

    keyword: str = ""

    page: int = 1

    limit: int = 20

    list_type: int = 2

    sort_type: int = 5

    shop_id: int | None = None

    item_id: int | None = None

    is_key_seller: bool = False

    is_ams_offer: bool = False

    shop_types: list[int] = field(default_factory=list)