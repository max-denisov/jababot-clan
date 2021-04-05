from vk_api.bot_longpoll import VkBotEventType

from Utils.PeopleQueue import PeopleQueue
from Utils.VKHelper import VKHelper, longpoll, helper
from config import JABABOT_ID
from control.Parser import Parser
from model.Command import command_dict


for event in longpoll.listen():  # Основной цикл
    if event.type == VkBotEventType.MESSAGE_NEW:  # Если пришло новое сообщение
        helper.set_chat_id(event.chat_id)

        text = str(event.message.text)
        print(text)  # TODO добавить логгер

        # команда пользователя
        if text.lower() in command_dict.values():
            PeopleQueue.push(event.message.from_id)  # id пользователя который вызвал команду
        # ответ бота
        for bot_command in command_dict.keys():
            if text.startswith(
                    bot_command.value):  # and event.message.from_id == JABABOT_ID:  # отключено на время тестирования
                if PeopleQueue.size():
                    Parser.parse_bot_command(bot_command, text)
                else:
                    helper.write_msg("Ошибка идентификации пользователя")
