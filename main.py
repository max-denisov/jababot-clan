from vk_api.bot_longpoll import VkBotEventType

from Utils.VKHelper import helperInstance, VKHelper
from config import JABABOT_ID
from control.Parser import Parser
from model.Command import command_dict

for event in helperInstance.longpoll.listen():  # Основной цикл
    if event.type == VkBotEventType.MESSAGE_NEW:  # Если пришло новое сообщение
        helperInstance.set_chat_id(event.chat_id)
        message = event.message
        message_str = helperInstance.get_message_str(message)
        print(message_str)  # TODO добавить логгер

        # команда пользователя
        if message_str.lower() in command_dict.values():  # если найдена валидная команда
            helperInstance.add_person(message.from_id)  # то сохраняется id юзера вызвавшего команду
        # команда бота
        for bot_command in command_dict.keys():
            if message_str.__contains__(bot_command.value) and VKHelper.is_message_from(message, JABABOT_ID):
                if helperInstance.get_queue_size() == 0:
                    helperInstance.write_msg("Ошибка идентификации пользователя")
                else:
                    Parser.parse_bot_command(bot_command, message_str)
                break
