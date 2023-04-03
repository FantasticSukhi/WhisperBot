from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

I am the Master of Whisperers messages means you can share hidden message to anyone .

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

To see how to use me press 'How to Use' below.

By @GORILLA_NETWORKS
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/GORILLA_BOTS")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/GORRILA_SUPPORT")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@WG_GBOT your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @GORILLA_NETWORK

Source Code : [Click Here](https://github.com/FantasticSukhi/WhisperBot)

Inspired By : nnbbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @MAMBA_RETURNS
    
