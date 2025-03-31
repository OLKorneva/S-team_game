from dataclasses import dataclass
from typing import Optional, List
from uuid import UUID

from src.core.entities import Effect
from src.core.entities.Item import ItemCategory, ItemRarity, Size, ItemID


@dataclass
class ItemResponseDTO:
    """
    DTO для передачи информации о предмете клиенту.
    """
    id: ItemID
    name: str # Название
    description: str # Описание
    category: ItemCategory  # Тип предмета (оружие, одежда и т.д.)
    rarity: ItemRarity  # Редкость предмета
    size: Size  # Размер предмета в слотах
    price: int  # Стоимость предмета в игровой валюте (?нужно?)
    effects: List[UUID]  # Список ID эффектов, которые накладывает предмет
    weight: float # Вес (?нужно?)
    durability: Optional[int] = None  # Прочность (если применимо)
    repair_count: Optional[int] = None  # Количество оставшихся ремонтов
    is_stackable: bool = False  # Можно ли складывать в один слот
    extra_slots: Optional[int] = None  # Дополнительные слоты (только для рюкзаков)