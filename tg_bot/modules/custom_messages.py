from tg_bot import dispatcher
from telegram import Update, Bot
from telegram.ext import CommandHandler, run_async, Filters
from tg_bot.modules.helper_funcs.chat_status import bot_admin, bot_can_delete, user_admin

### Replies with the information message which questions are being answered and how to hire a programmer
def display_lop(bot: Bot, update: Update):
	user = update.effective_user
	chat_id = update.effective_chat.id
	
	text = """
	Dear Community Member, we are willing to help you on all specific questions related to Telegram bots and programming of those.
	Though you need to know how to program. If you need some help on how to get started to program a bot, check our /links .
	
	Questions like "how i´m programming ..." will not be answered. 
	Instead ask something like "I´m using PHP and I want to program a [...] bot. I´m struggling on how to get the updates via Webhook.
	This is my code: [link to pastebin]". 
	
	If you are not willing to learn a programming language, you can hire another member.
	For that please describe exactly what your bot should do and how much you are willing to pay.
	Interested members will get in touch with you.
	"""
	update.effective_message.reply_text(text)		

@bot_admin
@bot_can_delete
@user_admin
### Deletes the sent message and repeats it	
def say(bot:Bot, update: Update):
	chat = update.effective_chat  # type: Optional[Chat]
	message_id = update.effective_message.message_id
	message = update.effective_message.text
	bot.deleteMessage(chat.id,message_id)
	bot.sendMessage(chat.id,message)

__help__ = """
 - /learnorpay or /lop Display the information message which questions are being answered and how to hire a programmer.
"""

__mod_name__ = "TBC Custom Messages"

LEARNORPAY_HANDLER = CommandHandler("learnorpay", display_lop, filters=Filters.group)
LOP_HANDLER = CommandHandler("lop", display_lop, filters=Filters.group)
SAY_HANDLER = CommandHandler("say",say,filters=Filters.group)

dispatcher.add_handler(LEARNORPAY_HANDLER)
dispatcher.add_handler(LOP_HANDLER)
dispatcher.add_handler(SAY_HANDLER)
