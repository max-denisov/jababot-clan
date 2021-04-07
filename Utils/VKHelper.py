from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id

from Utils.PeopleQueue import PeopleQueue
from config import VK_GROUP_ID
from api_token import TOKEN


class VKHelper:
    def __init__(self, token=TOKEN, group_id=VK_GROUP_ID):
        self.chat_id = 0
        # Авторизация
        self.api = vk_api.VkApi(token=token)
        # Работа с сообщениями
        self.longpoll = VkBotLongPoll(self.api, group_id)
        self._people_queue = PeopleQueue()

    def write_msg(self, message):
        self.api.method('messages.send', {'chat_id': self.chat_id, 'message': message, 'random_id': get_random_id()})

    def get_message_str(self, event):
        self.chat_id = event.chat_id  # TODO выделить в отдельный метод

        text = str(event.message.message_str)
        text = text.removeprefix("[club191097210|@toadbot] ")  # убирает упоминание бота при вызове кнопкой
        return text

    def add_person(self, person_id):
        self._people_queue.push(person_id)

    def get_queue_size(self):
        return self._people_queue.size()


helperInstance = VKHelper()
