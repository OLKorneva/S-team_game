from dataclasses import dataclass


class Effect:
    """Базовый класс для эффекта предмета на характеристики персонажа"""
    def apply(self, character) -> None:
        """Применяет эффект к персонажу"""
        pass

@dataclass
class StatBoostEffect(Effect):
    """Увеличение характеристики персонажа"""
    stat_name: str  # Имя характеристики (например, 'health', 'damage')
    value: float  # Сколько увеличивается

    def apply(self, character) -> None:
        """Применяет увеличение характеристики к персонажу"""
        if hasattr(character, self.stat_name):
            current_value = getattr(character, self.stat_name)
            setattr(character, self.stat_name, current_value + self.value)