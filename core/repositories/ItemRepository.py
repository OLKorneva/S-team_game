from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.entities.Item import ItemID
from src.core.repositories.dto import ItemCreateDTO, ItemResponseDTO, ItemUpdateDTO
from src.core.repositories.dto.ItemFilterDTO import ItemFilterDTO
from src.core.repositories.dto.ItemListDTO import ItemListDTO


class ItemRepository(ABC):
    """Интерфейс репозитория для работы с Item."""

    @abstractmethod
    async def get_by_item_id(self, item_id: ItemID) -> Optional[ItemResponseDTO]:
        """Получает Item по его ID."""
        pass

    @abstractmethod
    async def create(self, item_dto: ItemCreateDTO) -> ItemResponseDTO:
        """Создаёт новую вещь и возвращает ее данные."""
        pass

    @abstractmethod
    async def update(self, item_dto: ItemUpdateDTO) -> Optional[ItemResponseDTO]:
        """Обновляет существующую Item и возвращает обновлённые данные."""
        pass

    @abstractmethod
    async def delete(self, item_id: ItemID) -> None:
        """Удаляет Item по ее ID."""
        pass

    @abstractmethod
    async def find_items(self, filters: ItemFilterDTO) -> ItemListDTO:
        """Находит предметы по заданным фильтрам."""
        pass


'''
[получить каждую из характеристик: прочность и количество ремонтов, и т.д.]
[апдейт характеристик: прочность и количество ремонтов, или всех?]
'''

