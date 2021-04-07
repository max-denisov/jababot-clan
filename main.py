from vk_api.bot_longpoll import VkBotEventType

from Utils.Logger import log, error
from control.VKHelper import helperInstance, VKHelper
from config import JABABOT_ID
from control.Parser import Parser
from model.Command import command_dict
from model.Jaba import Jaba

for event in helperInstance.get_event_stream():  # Основной цикл
    if event.type == VkBotEventType.MESSAGE_NEW:
        helperInstance.set_chat_id(event.chat_id)
        message = event.message
        message_str = VKHelper.get_message_str(message)
        log.info(message_str)

        # кастомные команды
        if message_str.lower().startswith("дай инфо"):
            person_tag = message_str.lower().removeprefix("дай инфо")
            if person_tag:
                person_id = VKHelper.get_id_from_tag(person_tag)
            else:
                person_id = message.from_id
            VKHelper.write_msg(Jaba.get_full_info(person_id))

        # команда пользователя
        if message_str.lower() in command_dict.values():  # если найдена валидная команда
            helperInstance.add_person(message.from_id)  # то сохраняется id юзера вызвавшего команду
        # команда бота
        for bot_command in command_dict.keys():
            if message_str.__contains__(bot_command.value) and VKHelper.is_message_from(message, JABABOT_ID):
                if helperInstance.get_queue_size() == 0:
                    error("Ошибка идентификации пользователя")
                else:
                    Parser.parse_bot_command(bot_command, message_str)
                break
