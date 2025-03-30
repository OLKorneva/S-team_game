from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
from uuid import UUID

from src.core.entities import Effect


class ItemCategory(Enum):
    """Категории предметов"""
    CLOTHING = "clothing"  # Одежда
    ACCESSORY = "accessory"  # Украшения и гаджеты
    WEAPON = "weapon"  # Оружие
    BOOSTER = "booster"  # Усиляторы
    CONSUMABLE = "consumable"  # Расходники
    CRAFTING = "crafting"  # Крафт
    BACKPACK = "backpack"  # Рюкзаки
    QUEST = "quest"  # Квестовые (?могут быть одновременно и другой категории или нет?)


class ItemRarity(Enum):  # нужно это?
    """Редкость предмета"""
    COMMON = "common"  # Обычный
    UNCOMMON = "uncommon"  # Необычный
    RARE = "rare"  # Редкий
    EPIC = "epic"  # Эпический
    LEGENDARY = "legendary"  # Легендарный


@dataclass(frozen=True)
class ItemID:
    """Уникальный идентификатор предмета"""
    value: UUID


@dataclass(frozen=True)
class Size:
    width: int  # Ширина в слотах
    height: int  # Высота в слотах

    def area(self) -> int:
        """Возвращает количество занятых слотов"""
        return self.width * self.height


@dataclass
class Item:
    """Базовая сущность предмета"""
    id: ItemID
    name: str  # Название
    description: str  # Описание
    category: ItemCategory  # Тип предмета (оружие, одежда и т. д.)
    rarity: ItemRarity  # Редкость предмета
    size: Size  # Размер предмета в слотах
    price: int  # Стоимость предмета в игровой валюте (?нужно?)
    weight: float  # Вес (?нужно?)
    durability: Optional[int] = None  # Прочность (если применимо)
    repair_count: Optional[int] = None  # Количество оставшихся ремонтов
    is_stackable: bool = False  # Можно ли складывать в один слот
    effects: List[Effect] = None  # Эффекты, которые накладывает предмет

    def is_equippable(self) -> bool:
        """Можно ли надеть предмет на персонажа"""
        return self.category in {ItemCategory.CLOTHING, ItemCategory.ACCESSORY, ItemCategory.WEAPON}

    def is_consumable(self) -> bool:
        """Можно ли употребить предмет"""
        return self.category in {ItemCategory.CONSUMABLE, ItemCategory.BOOSTER}


@dataclass
class Backpack(Item):
    """Рюкзак — предмет, который увеличивает количество слотов в инвентаре"""
    extra_slots: int = 5  # Дефолтное значение для увеличения слотов (например, 5 дополнительных слотов)
