from Utils.PeopleQueue import PeopleQueue
from Utils.VKHelper import helper
from model.Command import Command
from model.Gear import Gear


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
    def handle_gear(gear_str):
        info_str = ''
        for stat in Gear:
            parsed_stat = Parser.parse_value(gear_str, stat.value)
            info_str += stat.value + ' ' + parsed_stat + '\n'
        helper.write_msg(info_str)

    @staticmethod
    def parse_bot_command(command_type, command_str):
        command_str += '\n'  # перенос строки в конце для парсинга
        if command_type == Command.JABA:
            Parser.handle_jaba(command_str)
        elif command_type == Command.GEAR:
            Parser.handle_gear(command_str)
        else:
            helper.write_msg("Неизвестная команда жабабота")
