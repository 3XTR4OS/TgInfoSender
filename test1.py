from telethon import TelegramClient
import BOT_INFO

API_ID = BOT_INFO.API_ID  # вида: 12345678
API_HASH = BOT_INFO.API_HASH  # вида: '12345q1wer23t51q123.....'


def sender(message, to_all_users=False):
    """
    Функция, доставляет нужное сообщение вашим контактам.
    Если to_all_users = False, то сообщение отправится только тем контактам,
    которые находятся в списке "согласились на рассылку"
    """

    if to_all_users:
        users = BOT_INFO.users_all
    else:
        users = BOT_INFO.users_mailing

    with TelegramClient('anon', API_ID, API_HASH) as client:
        for user in users:
            client.loop.run_until_complete(client.send_message(user, message))


sender(message='маленький тест', to_all_users=True)
