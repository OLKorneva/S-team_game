from dataclasses import dataclass
from typing import Optional

from src.core.entities.Item import ItemCategory, ItemRarity


@dataclass
class ItemFilterDTO:
    """
    DTO для фильтрации списка предметов.
    """
    category: Optional[ItemCategory] = None
    rarity: Optional[ItemRarity] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None