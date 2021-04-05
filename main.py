import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from config import token


def write_msg(chat_id, message):
    vk.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': get_random_id()})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkBotLongPoll(vk, group_id=203787709)

print('foo')

# Основной цикл
for event in longpoll.listen():
    print(event.type)
    # Если пришло новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        # Сообщение от пользователя
        request = str(event.message.text)
        print(request)

        if request.startswith("Запомнить клан "):
            clan_name = request[len("Запомнить клан "):]
            write_msg(event.chat_id, "Ваш клан - " + clan_name)
        else:
            write_msg(event.chat_id, "Не поняла вашего ответа...")
