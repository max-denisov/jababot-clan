from vk_api.bot_longpoll import VkBotEventType

from Utils.VKHelper import helperInstance
from config import JABABOT_ID
from control.Parser import Parser
from model.Command import command_dict

for event in helperInstance.longpoll.listen():  # Основной цикл
    if event.type == VkBotEventType.MESSAGE_NEW:  # Если пришло новое сообщение
        message_str = helperInstance.get_message_str(event)
        print(message_str)  # TODO добавить логгер

        # команда пользователя
        if message_str.lower() in command_dict.values():  # если найдена валидная команда
            helperInstance.add_person(event.message.from_id)  # то сохраняется id юзера вызвавшего команду
        # команда бота
        for bot_command in command_dict.keys():
            if message_str.__contains__(bot_command.value) and event.message.from_id == JABABOT_ID:
                if helperInstance.get_queue_size() == 0:
                    helperInstance.write_msg("Ошибка идентификации пользователя")
                else:
                    Parser.parse_bot_command(bot_command, message_str)
