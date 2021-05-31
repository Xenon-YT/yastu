# YASTU - Yet Another Simple Telegram Userbot.
Just another Python simple Telegram userbot code.

## How to install it
    pip install python-telegram
    git clone https://github.com/at0mdud3/yastu.git yastu
Then create a [Telegram Application](my.telegram.org) and save the API Id and the API Hash.
After creating the application edit `yastu.py`'s login settings like this:

    tg = Telegram(
    api_id='your API ID',
    api_hash='your API Hash',
    phone="userbot's phone number",
    database_encryption_key='changeme'
    )
Then edit the code as you want, save it and run in bash:

    python yastu.py

Follow the login instructions in log and enjoy!

## Credits
[Alexander Akhmetov](https://github.com/alexander-akhmetov/python-telegram);
[Telegram](https://core.telegram.org/tdlib);
