from enum import Enum

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from config import token


class Commands(Enum):
    JABA = "🐸Имя вашей жабы:"
    INVENTORY = "Ваше снаряжение:"


def write_msg(chat_id, message):
    vk.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': get_random_id()})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkBotLongPoll(vk, group_id=203787709)


def parse_value(text, parameter_str):
    start_index = text.find(parameter_str) + len(parameter_str)
    return text[start_index:text.find('\n', start_index)]


people_id = []
commands = {
    Commands.JABA: "моя жаба",
    Commands.INVENTORY: "мое снаряжение",
}
JABABOT_ID = -191097210


def handle_jaba(jaba_str):
    name = parse_value(jaba_str, "🐸Имя вашей жабы: ")
    level = parse_value(jaba_str, "⭐Уровень вашей жабы: ")
    write_msg(event.chat_id, "Это жаба " + str(people_id.pop(0)) + ", " + name + " " + level + "уровня")


def handle_inventory(inventory_str):
    melee = parse_value(inventory_str, "🗡Ближний бой: ")
    ranged = parse_value(inventory_str, "🏹Дальний бой: ")
    write_msg(event.chat_id, "Оружие " + str(people_id.pop(0)) + ", " + melee + " и " + ranged)


def parse_bot_command(command_type, command_str):
    if command_type == Commands.JABA:
        handle_jaba(command_str)
    elif command_type == Commands.INVENTORY:
        handle_inventory(command_str)
    else:
        write_msg(event.chat_id, "Неизвестная команда жабабота")


# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        # Сообщение от пользователя
        text = str(event.message.text)
        print(text)
        # команда пользователя
        if text.lower() in commands.values():
            people_id.append(event.message.from_id)
        # ответ бота
        for bot_command in commands.keys():
            if text.startswith(bot_command.value): # and event.message.from_id == JABABOT_ID:  # отключено на время тестирования
                if len(people_id):
                    parse_bot_command(bot_command, text)
                else:
                    write_msg(event.chat_id, "Ошибка идентификаци пользователя")
