from telethon import TelegramClient

API_ID = 123456
API_HASH = '123456qwerty123456'
users = [
    'user1',
    'user2',
    'user3'
]


class Mailing:
    def __init__(self):
        self.API_ID = 123456
        self.API_HASH = '123456qwerty123456'
        self.message_default_body = '/СГЕНЕРИРОВАНО АВТОМАТИЧЕСКИ/'
        self.message = ''


with TelegramClient('anon', API_ID, API_HASH) as client:
    # Первый параметр - это имя файла.session (появляется в каталоге проекта)
    for user in users:
        client.loop.run_until_complete(client.send_message(user,
                                                           '/CГЕНЕРИРОВАНО АВТОМАТИЧЕСКИ/ \n'
                                                           '/ГАЛАКТИЧЕСКИМ ВОЙСКОМ/ \n'
                                                           'ЛЮДИ!!! \n'
                                                           'Вам. Всем. Конец!'))
