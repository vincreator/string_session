from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
~ Check your Telegram saved messages section to copy the STRING_SESSION
""")
API_KEY = int(input("Enter API_KEY here: "))
API_HASH = input("Enter API_HASH here: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check your Telegram Saved Messages to copy the STRING_SESSION value")
    session_string = client.session.save()
    saved_messages_template = """Support: @userbotindo

<b>STRING_SESSION</b>: <code>{}</code>

⚠️ <i>Please be carefull to pass this value to third parties</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")