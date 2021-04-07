from Utils.Logger import error
from Utils.VKHelper import helperInstance
from model.Command import Command
from model.Gear import Gear
from model.MyJaba import MyJaba


class Parser:
    @staticmethod
    def parse_bot_command(command_type, command_str):
        command_str += '\n'  # перенос строки в конце для парсинга
        if command_type == Command.JABA:
            Parser._handle_jaba(command_str)  # TODO создать общий метод обработки
        elif command_type == Command.GEAR:
            Parser._handle_gear(command_str)
        else:
            error("Неизвестная команда жабабота")

    @staticmethod
    def _handle_jaba(jaba_str):
        jaba_list = Parser._parse_all_stats(MyJaba, jaba_str)  # TODO переименовать
        Parser._message_stat(jaba_list)

    @staticmethod
    def _handle_gear(gear_str):
        gear_list = Parser._parse_all_stats(Gear, gear_str)
        Parser._message_stat(gear_list)

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
    def _message_stat(stat_list):
        info_str = ''
        for stat in stat_list:
            info_str += f'{stat[0].value} {stat[1]}\n'
        helperInstance.write_msg(info_str)
