from Utils.PeopleQueue import PeopleQueue
from Utils.VKHelper import helper
from model.Command import Command


class Parser:
    @staticmethod
    def parse_value(text, parameter_str):
        parameter_start = text.find(parameter_str)
        if parameter_start == -1:
            return "Ошибка парсинга"  # TODO в логгер
        parameter_end = parameter_start + len(parameter_str)
        return text[parameter_end:text.find('\n', parameter_end)]

    @staticmethod
    def handle_jaba(jaba_str):
        name = Parser.parse_value(jaba_str, "Имя вашей жабы: ")
        level = Parser.parse_value(jaba_str, "Уровень вашей жабы: ")
        helper.write_msg("Это жаба " + str(PeopleQueue.pull()) + ", " + name + " " + level + "уровня")

    @staticmethod
    def handle_inventory(inventory_str):
        inventory = {  # TODO в Enum
            "melee": "Ближний бой: ",
            "ranged": "Дальний бой: ",
            "head": "Наголовник: ",
            "chest": "Нагрудник: ",
            "legs": "Налапники: ",
            "team": "Банда: ",
            "weapon_pieces": "Оружейных кусочков: ",
            "t1_pieces": "Кусочков водорослей: ",
            "t2_pieces": "Кусочков кувшинки: ",
            "t3_pieces": "Кусочков клюва цапли: ",
            "hp": "Здоровье:",
            "attack": "Атака:",
            "defence": "Защита:"
        }
        stats = []
        for stat_name in inventory.keys():
            stats.append((inventory.get(stat_name), Parser.parse_value(inventory_str, inventory.get(stat_name))))
            print(stats[-1])

        info_str = ''
        for stat in stats:
            info_str += stat[0] + stat[1] + '\n'
        helper.write_msg(info_str)

    @staticmethod
    def parse_bot_command(command_type, command_str):
        if command_type == Command.JABA:
            Parser.handle_jaba(command_str)
        elif command_type == Command.INVENTORY:
            Parser.handle_inventory(command_str)
        else:
            helper.write_msg("Неизвестная команда жабабота")
