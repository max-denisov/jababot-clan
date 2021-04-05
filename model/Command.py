from enum import Enum


class Command(Enum):
    JABA = "🐸Имя вашей жабы:"
    INVENTORY = "Ваше снаряжение:"


command_dict = {
    Command.JABA: "моя жаба",
    Command.INVENTORY: "мое снаряжение",
}
