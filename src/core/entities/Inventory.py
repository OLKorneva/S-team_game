import uuid
from dataclasses import dataclass
from typing import List, Tuple, Any

from src.core.entities.Item import Item


@dataclass(frozen=True)
class InventorySize:
    """Value object для размера инвентаря"""
    width: int
    height: int

    def __post_init__(self) -> None:
        """Проверка на корректность размера инвентаря"""
        if self.width < 1:
            raise ValueError("Ширина инвентаря должна быть больше нуля")
        if self.height < 1:
            raise ValueError("Высота инвентаря должна быть больше нуля")

    def get_area(self) -> int:
        """Возвращает количество занятых слотов"""
        return self.width * self.height

    def __str__(self) -> str:
        return f"{self.width}x{self.height}"


@dataclass(frozen=True)
class InventoryID:
    """Value object для уникального идентификатора инвентаря"""
    value: uuid.UUID

    @staticmethod
    def generate() -> "InventoryID":
        """Фабричный метод для генерации уникального идентификатора инвентаря"""
        return InventoryID(uuid.uuid4())

    def __str__(self) -> str:
        return str(self.value)


class Inventory:
    """Сущность инвентаря"""

    def __init__(self, width: int, height: int) -> None:
        self.id = InventoryID.generate()
        self._size: InventorySize = InventorySize(width, height)
        self._items: List[Item] = []
        self._slot_matrix: List[List[Any]] = [[0] * width for _ in range(height)]

    @property
    def items(self) -> Tuple[Item, ...]:
        """Возвращает список предметов в инвентаре"""
        return tuple(self._items)

    @property
    def slot_matrix(self) -> Tuple[Tuple[int, ...], ...]:
        """Возвращает матрицу слотов в инвентаре"""
        return tuple(tuple(row) for row in self._slot_matrix)

    def get_tuple_coordinates_available_slots(self) -> Tuple[Tuple[int, int], ...]:
        """Возвращает кортеж координат доступных слотов"""
        available_slots: List[Tuple[int, int]] = []

        for i in range(self._size.height):
            for j in range(self._size.width):
                if self._slot_matrix[i][j] == 0:
                    available_slots.append((i, j))

        return tuple(available_slots)

    @property
    def is_overcrowded(self) -> bool:
        """Возвращает True, если инвентарь переполнен"""
        return not self.get_tuple_coordinates_available_slots()

    @property
    def count_items(self) -> int:
        """Возвращает количество предметов в инвентаре"""
        return len(self.items)

    def can_place_item(self, item: Item, x: int, y: int) -> bool:
        """Проверяет можно ли поместить предмет в указанных координаты"""
        if (x + item.size.height > self._size.height or
                y + item.size.width > self._size.width):
            return False

        for i in range(x, x + item.size.height):
            for j in range(y, y + item.size.width):
                if self._slot_matrix[i][j] != 0:
                    return False
        return True

    def add_item(self, item: Item, x: int, y: int) -> None:
        """Добавляет предмет в инвентарь"""

        if not self.can_place_item(item, x, y):
            raise ValueError("Нельзя разместить предмет в указанных координатах")

        for i in range(x, x + item.size.height):
            for j in range(y, y + item.size.width):
                self._slot_matrix[i][j] = item.name

        self._items.append(item)

    def remove_item(self, item: Item, x: int, y: int) -> None:
        """Удаляет предмет из инвентаря"""
        if item not in self._items:
            raise ValueError("Предмет не найден в инвентаре")

        for i in range(x, x + item.size.height):
            for j in range(y, y + item.size.width):
                self._slot_matrix[i][j] = 0

        self._items.remove(item)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, size={self._size})"


for row in Inventory(7, 4).slot_matrix:
    print(row)
