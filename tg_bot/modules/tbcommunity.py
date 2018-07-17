from telegram import Message, Update, Bot, User
from telegram import ParseMode, MAX_MESSAGE_LENGTH
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown
from telegram.ext import CommandHandler

import tg_bot.modules.sql.userinfo_sql as sql
from tg_bot import dispatcher, SUDO_USERS
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.extraction import extract_user

RESOURCES_LINK = """
⭕️ Some helpfull links to start learning Telegram Bot with php : 

✅ Youtube video : 
Telegram Bot Tutorial - YouTube : 
https://www.youtube.com/watch?v=hJBYojK7DO4

Set your Telegram Bot Webhook using this Bot :
https://www.youtube.com/watch?v=4BJqfyHbVlw

How to use Commands with Telegram Bots - YouTube :
https://www.youtube.com/watch?v=ry6YGBPeuig

How to create Telegram Bots :
https://www.youtube.com/watch?v=xB_QeZm7dFY

✅ Website links : 
How to Build Fully Responsive Telegram Bot – PHP Tutorial : 
https://www.lifeofgeek.com/fully-responsive-telegram-bot-php-tutorial/

How to Start a Telegram Bot With PHP : 
https://code.tutsplus.com/articles/how-to-start-a-telegram-bot-with-php--cms-26329

TUTORIALS LINKS FOR TELEGRAM BOTS : 
https://botwiki.org/tutorials/telegram-bots/
http://telegramgeeks.com/2015/09/tutorials-for-bots/

Very Basic PHP Telegram Bot w/Webhooks : 
http://blog.stickyrice.net/archives/2015/very-basic-php-telegram-bot-wwebhooks/

✅ Telegram Bot Reference : 
Telegram Bot API : 
https://core.telegram.org/bots/api

Bot Code Examples :
https://core.telegram.org/bots/samples

Telegram Bots Code Examples - Hellobot : (Very Helpfull) 
https://core.telegram.org/bots/samples/hellobot

✅ For iranian Users :  (Persian Language)
Let's play with Telegram Bot API : 
http://ashiyane.org/forums/showthread.php?146845-Let-s-play-with-Telegram-Bot-API

✅ For answer of your other questions :
+ This Group : https://telegram.me/joinchat/AOmo4jzvT2L6_PLrLApWqQ
+ http://google.com
+ http://youtube.com
+ http://codeacademy.com
+ https://stackoverflow.com
"""

__help__ = """
/links - Get a list of resources that will help you learn to code
"""

__mod_name__ = "Coding Help"

@run_async
def get_resources(bot, update):
    update.message.reply_text(RESOURCES_LINK)
    
resources_handler = CommandHandler('links', get_resources)

dispatcher.add_handler(resources_handler)
    