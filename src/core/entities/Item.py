from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
from uuid import UUID

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


class ItemRarity(Enum): # нужно это?
    """Редкость предмета"""
    COMMON = "common"       # Обычный
    UNCOMMON = "uncommon"   # Необычный
    RARE = "rare"           # Редкий
    EPIC = "epic"           # Эпический
    LEGENDARY = "legendary" # Легендарный


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

    def is_equippable(self) -> bool:
        """Можно ли надеть предмет на персонажа"""
        return self.category in {ItemCategory.CLOTHING, ItemCategory.ACCESSORY, ItemCategory.WEAPON}

    def is_consumable(self) -> bool:
        """Можно ли употребить предмет"""
        return self.category in {ItemCategory.CONSUMABLE, ItemCategory.BOOSTER}


[по уровню, по классу подходит, что-то позволяет носить шляпу, ] - в сервисе надевания шляпы
со стягивания с себя - в рюкзак или сразу продать

контексы - юз.кейсы - на каком уровне они находятся
проверка бизнес-логики в сервисе или он отвечает за взаимодейстие
где точка пересечения контекстов

юз кейсы локальные/глобальные

вещь не может быть без места, взаимодействия с ней могут быть разные в разных местах. у нпс - купить,
у пользователя - продать (может ли продать, сколько получит - доменный сервис)

use case - торговля -стоит выше и модет опустится на уровень ниже
внутри домена (внутренний кружочек), а контекст - весь пирок на части с всеми слоями.
