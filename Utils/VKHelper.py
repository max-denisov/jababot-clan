from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id

from config import VK_GROUP_ID
from api_token import _TOKEN

# Авторизация
_vk = vk_api.VkApi(token=_TOKEN)

# Работа с сообщениями
longpoll = VkBotLongPoll(_vk, VK_GROUP_ID)


class VKHelper:
    def __init__(self, chat_id=0):
        self.chat_id = chat_id

    def write_msg(self, message):
        _vk.method('messages.send', {'chat_id': self.chat_id, 'message': message, 'random_id': get_random_id()})

    def set_chat_id(self, id):
        self.chat_id = id


helper = VKHelper()
