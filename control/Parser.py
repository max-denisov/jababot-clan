from Utils.PeopleQueue import PeopleQueue
from Utils.VKHelper import helper
from model.Command import Command


class Parser:
    @staticmethod
    def parse_value(text, parameter_str):
        start_index = text.find(parameter_str) + len(parameter_str)
        return text[start_index:text.find('\n', start_index)]

    @staticmethod
    def handle_jaba(jaba_str):
        name = Parser.parse_value(jaba_str, "🐸Имя вашей жабы: ")
        level = Parser.parse_value(jaba_str, "⭐Уровень вашей жабы: ")
        helper.write_msg("Это жаба " + str(PeopleQueue.pull()) + ", " + name + " " + level + "уровня")

    @staticmethod
    def handle_inventory(inventory_str):
        melee = Parser.parse_value(inventory_str, "🗡Ближний бой: ")
        ranged = Parser.parse_value(inventory_str, "🏹Дальний бой: ")
        helper.write_msg("Оружие " + str(PeopleQueue.pull()) + ", " + melee + " и " + ranged)

    @staticmethod
    def parse_bot_command(command_type, command_str):
        if command_type == Command.JABA:
            Parser.handle_jaba(command_str)
        elif command_type == Command.INVENTORY:
            Parser.handle_inventory(command_str)
        else:
            helper.write_msg("Неизвестная команда жабабота")