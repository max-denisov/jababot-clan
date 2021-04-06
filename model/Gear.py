from enum import Enum


class Gear(Enum):
    MELEE = "Ближний бой: "
    RANGED = "Дальний бой: "
    HEAD = "Наголовник: "
    CHEST = "Нагрудник: "
    LEGS = "Налапники: "
    TEAM = "Банда: "
    WEAPON_PIECES = "Оружейных кусочков: "
    T1_PIECES = "Кусочков водорослей: "
    T2_PIECES = "Кусочков кувшинки: "
    T3_PIECES = "Кусочков клюва цапли:"
    HP = "Здоровье:"
    ATTACK = "Атака:"
    DEFENCE = "Защита:"
