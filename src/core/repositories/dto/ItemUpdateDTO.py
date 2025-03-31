from dataclasses import dataclass
from typing import Optional, List

from src.core.entities import Effect
from src.core.entities.Item import ItemID, ItemCategory, ItemRarity, Size


@dataclass
class ItemUpdateDTO:
    """
    DTO для обновления данных предмета.
    """
    id: ItemID
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[ItemCategory] = None
    rarity: Optional[ItemRarity] = None
    size: Optional[Size] = None
    price: Optional[int] = None
    weight: Optional[float] = None
    durability: Optional[int] = None
    repair_count: Optional[int] = None
    is_stackable: Optional[bool] = None
    effects: Optional[List[Effect]] = None
    extra_slots: Optional[int] = None  # Дополнительные слоты (только для рюкзаков)