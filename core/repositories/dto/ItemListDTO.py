from dataclasses import dataclass
from typing import List

from src.core.repositories.dto.ItemResponseDTO import ItemResponseDTO


@dataclass
class ItemListDTO:
    """
    DTO для передачи списка предметов.
    """
    items: List[ItemResponseDTO]