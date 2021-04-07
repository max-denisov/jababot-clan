from Utils.PeopleQueue import PeopleQueue
from Utils.VKHelper import helper
from model.Command import Command
from model.Gear import Gear
from model.MyJaba import MyJaba


class Parser:
    @staticmethod
    def parse_bot_command(command_type, command_str):
        command_str += '\n'  # перенос строки в конце для парсинга
        if command_type == Command.JABA:
            Parser.handle_jaba(command_str)  # TODO создать общий метод обработки
        elif command_type == Command.GEAR:
            Parser.handle_gear(command_str)
        else:
            helper.write_msg("Неизвестная команда жабабота")
            return

    @staticmethod
    def handle_jaba(jaba_str):
        jaba_list = Parser.parse_all_stats(MyJaba, jaba_str)
        Parser.message_stat(jaba_list)

    @staticmethod
    def handle_gear(gear_str):
        gear_list = Parser.parse_all_stats(Gear, gear_str)
        Parser.message_stat(gear_list)

    @staticmethod
    def parse_all_stats(stat_list, command_str):
        parsed_list = []
        for stat in stat_list:
            parsed_stat = Parser.parse_value(command_str, stat.value)
            parsed_list.append((stat, parsed_stat))
        return parsed_list

    @staticmethod
    def parse_value(text, parameter_str):
        parameter_start = text.find(parameter_str)
        if parameter_start == -1:
            return "Ошибка парсинга"  # TODO в логгер
        parameter_end = parameter_start + len(parameter_str)
        return text[parameter_end:text.find('\n', parameter_end)]

    @staticmethod
    def message_stat(stat_list):
        info_str = ''
        for stat in stat_list:
            info_str += stat[0].value + ' ' + stat[1] + '\n'
        helper.write_msg(info_str)
