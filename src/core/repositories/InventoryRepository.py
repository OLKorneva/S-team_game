from abc import ABC, abstractmethod
from typing import Tuple, Optional

from src.core.entities.Inventory import InventoryID
from src.core.repositories.dto import InventoryUpdateDTO, InventoryCreateDTO, InventoryResponseDTO, ItemResponseDTO


class InventoryRepository(ABC):
    """Интерфейс репозитория для работы с инвентарями."""

    @abstractmethod
    async def create(self, inventory_dto: InventoryCreateDTO) -> InventoryResponseDTO:
        """Создаёт инвентарь и возвращает его данные."""
        ...

    @abstractmethod
    async def get_by_id(self, inventory_id: InventoryID) -> Optional[InventoryResponseDTO]:
        """Возвращает инвентарь по ID."""
        ...

    @abstractmethod
    async def get_by_owner(self, owner_id: ...) -> InventoryResponseDTO:
        """Получить инвентарь по владельцу"""
        pass

    @abstractmethod
    async def update(self, inventory_dto: InventoryUpdateDTO) -> InventoryResponseDTO:
        """Обновляет инвентарь и возвращает обновлённые данные."""
        ...

    @abstractmethod
    async def delete(self, inventory_id: InventoryID) -> None:
        """Удаляет инвентарь по его ID."""
        ...

    @abstractmethod
    async def get_all(self) -> Tuple[InventoryResponseDTO]:
        """Возвращает кортеж всех инвентарей."""
        ...

    @abstractmethod
    async def add_item(
        self,
        inventory_id: InventoryID,
        item: ItemResponseDTO,
        x: int,
        y: int
    ) -> InventoryResponseDTO:
        """Добавить предмет в инвентарь"""
        pass

    @abstractmethod
    async def remove_item(
        self,
        inventory_id: InventoryID,
        item: ItemResponseDTO
    ) -> InventoryResponseDTO:
        """Удалить предмет из инвентаря"""
        pass

    @abstractmethod
    async def move_item(
        self,
        inventory_id: InventoryID,
        item_id: ItemResponseDTO,
        new_x: int,
        new_y: int
    ) -> InventoryResponseDTO:
        """Переместить предмет в инвентаре"""
        pass

    @abstractmethod
    async def get_items(self, inventory_id: InventoryID) -> Tuple[ItemResponseDTO]:
        """Возвращает кортеж всех предметов в инвентаре"""
        pass
