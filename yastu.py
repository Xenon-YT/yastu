
from telegram.client import Telegram

tg = Telegram(
    api_id='',
    api_hash='',
    phone='',
    database_encryption_key='changeme'
)

tg.login()

def new_message_handler(update):
    message_content = update['message']['content'].get('text', {})
    message_text = message_content.get('text', '').lower()

    if message_text == 'Test!':
        chat_id = update['message']['chat_id']
        print(f'Someone called me in {chat_id}!')
        tg.send_message(
            chat_id=chat_id,
            text='This is just a test!',
        )

tg.add_message_handler(new_message_handler)
tg.idle()
