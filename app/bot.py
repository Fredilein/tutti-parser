from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from models import user, subscription
from credentials import creds

updater = Updater(token=creds['bot'], use_context=True)


# ENDPOINTS for the telegram bot
def start(update, context):
    user.new(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Yoo, use /sub to subscribe to queries.")


def sub(update, context):
    # Callback data is currently the id in the sql queries table
    keyboard = [[InlineKeyboardButton("Sonos", callback_data='1')],
                [InlineKeyboardButton("Philips Hue", callback_data='2')],
                [InlineKeyboardButton("EF 70-200mm", callback_data='3')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Choose query:', reply_markup=reply_markup)


# CALLBACK FUNCTION when selecting query to watch
def subscription_callback(update, context):
    query = update.callback_query

    u = user.get_from_chat_id(update.effective_chat.id)
    new_sub = subscription.new(u['id'], query.data)

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    if new_sub:
        query.edit_message_text(text='Successfully subscribed!')
    else:
        query.edit_message_text(text='Already subscribed')


# SEND MESSAGES without replying to a user
def send_all(msg):
    users = user.all()
    for u in users:
        updater.bot.send_message(chat_id=u[1], text=msg)


def send_item(item, chat_id):
    updater.bot.send_message(chat_id=chat_id, text=item, parse_mode="HTML")


# HANDLER for each endpoint of the bot
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(subscription_callback))
updater.dispatcher.add_handler(CommandHandler('sub', sub))

# Start the Bot
updater.start_polling()
