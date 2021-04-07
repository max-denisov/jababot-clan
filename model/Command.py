from enum import Enum


class Command(Enum):
    JABA = "Имя вашей жабы:"
    GEAR = "Ваше снаряжение:"


command_dict = {
    Command.JABA: "моя жаба",
    Command.GEAR: "мое снаряжение",
}
