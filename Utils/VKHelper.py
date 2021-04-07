from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id

from Utils.PeopleQueue import PeopleQueue
from config import VK_GROUP_ID, JABABOT_ID
from api_token import TOKEN


class VKHelper:
    def __init__(self, token=TOKEN, group_id=VK_GROUP_ID):
        self._chat_id = 0
        # Авторизация
        self._api = vk_api.VkApi(token=token)
        # Работа с сообщениями
        self._longpoll = VkBotLongPoll(self._api, group_id)
        self._people_queue = PeopleQueue()

    def write_msg(self, message):
        self._api.method('messages.send', {'chat_id': self._chat_id, 'message': message, 'random_id': get_random_id()})

    def set_chat_id(self, chat_id):
        self._chat_id = chat_id

    @staticmethod
    def get_message_str(message):
        text = str(message.text)
        text = text.removeprefix("[club191097210|@toadbot] ")  # убирает упоминание бота при вызове кнопкой
        return text

    def add_person(self, person_id):
        self._people_queue.push(person_id)

    def get_person(self):
        return self._people_queue.pull()

    def get_queue_size(self):
        return self._people_queue.size()

    @staticmethod
    def is_message_from(message, person_id):
        return message.from_id == person_id

    @staticmethod
    def get_id_from_tag(tag_text):
        start = tag_text.find('id') + len('id')
        end = tag_text.find('|')
        if end == -1:
            end = len(tag_text)
        return int(tag_text[start: end])

    def get_event_stream(self):
        return self._longpoll.listen()


helperInstance = VKHelper()
