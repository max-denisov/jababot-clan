import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


def write_msg(chat_id, message):
    vk.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': get_random_id()})


# API-ключ созданный ранее
token = "7d3585b1a64101223ccb263ab72adf686b5422e61d0be1650f15aa8e0655fde8e7c23670d5dc757ee88c6"

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
