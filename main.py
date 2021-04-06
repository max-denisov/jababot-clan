from vk_api.bot_longpoll import VkBotEventType

from Utils.PeopleQueue import PeopleQueue
from Utils.VKHelper import longpoll, helper, VKHelper
from config import JABABOT_ID
from control.Parser import Parser
from model.Command import command_dict

for event in longpoll.listen():  # Основной цикл
    if event.type == VkBotEventType.MESSAGE_NEW:  # Если пришло новое сообщение
        text = VKHelper.get_message_str(event)
        print(text)  # TODO добавить логгер

        # команда пользователя
        if text.lower() in command_dict.values():
            PeopleQueue.push(event.message.from_id)  # id пользователя который вызвал команду
        # команда бота
        for bot_command in command_dict.keys():
            if text.startswith(bot_command.value) and event.message.from_id == JABABOT_ID:
                if PeopleQueue.size():
                    Parser.parse_bot_command(bot_command, text)
                else:
                    helper.write_msg("Ошибка идентификации пользователя")
