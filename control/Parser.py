from Utils.Logger import error
from Utils.VKHelper import helperInstance
from model.Command import Command
from model.Gear import Gear
from model.Jaba import Jaba
from model.MyJaba import MyJaba


class Parser:
    @staticmethod
    def parse_bot_command(command_type, command_str):
        command_str += '\n'  # перенос строки в конце для парсинга
        if command_type == Command.JABA:
            handled_enum = MyJaba
            handled_method = Jaba.set_my_jaba
        elif command_type == Command.GEAR:
            handled_enum = Gear
            handled_method = Jaba.set_gear
        else:
            error("Неизвестная команда жабабота")
            return
        stat_str = Parser._handle_stat(handled_enum, command_str)
        handled_method(helperInstance.get_person(), stat_str)

    @staticmethod
    def _handle_stat(enum_class, stat_str):
        stat_list = Parser._parse_all_stats(enum_class, stat_str)
        return Parser.stat_to_str(stat_list)

    @staticmethod
    def _parse_all_stats(stat_list, command_str):
        parsed_list = []
        for stat in stat_list:
            parsed_stat = Parser._parse_value(command_str, stat.value)
            parsed_list.append((stat, parsed_stat))
        return parsed_list

    @staticmethod
    def _parse_value(text, parameter_str):
        parameter_start = text.find(parameter_str)
        if parameter_start == -1:
            error("Ошибка парсинга")
            return "Не распознано"
        parameter_end = parameter_start + len(parameter_str)
        return text[parameter_end:text.find('\n', parameter_end)]

    @staticmethod
    def stat_to_str(stat_list):
        info_str = ''
        for stat in stat_list:
            info_str += f'{stat[0].value} {stat[1]}\n'
        return info_str
