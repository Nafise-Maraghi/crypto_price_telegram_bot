from telegram import *
from telegram.ext import *
from tradingview_ta import TA_Handler, Interval, Exchange

from key import token


# start(Boolian): is it a "/start" command or not
def main_menu(start, update, context):
    buttons = [
        [KeyboardButton("Bitcoin (BTC)")], 
        [KeyboardButton("Ethereum (ETH)")], 
        [KeyboardButton("Tether (USDT)")], 
        [KeyboardButton("Binance Coin (BNB)")], 
        [KeyboardButton("U.S. Dollar Coin (USDC)")], 
        [KeyboardButton("Ripple (XRP)")], 
        [KeyboardButton("Binance USD (BUSD)")], 
        [KeyboardButton("Cardano (ADA)")], 
        [KeyboardButton("Dogecoin (DOGE)")], 
        [KeyboardButton("Solana (SOL)")], 
        ]
    
    if start:
        message = "Hello and welcome!\nPlease choose a cryptocurrency 🪙:"

    else:
        message = "Please choose a cryptocurrency:"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=ReplyKeyboardMarkup(buttons))


def start_function(update, context):
    main_menu(True, update, context)


# Connecting our app with the Telegram API Key and using the context
updater = Updater(token, use_context=True)
my_dispacher = updater.dispatcher

# Adding CommandHandler from telegram.ext to handle defined functions/commands
my_dispacher.add_handler(CommandHandler("start", start_function))

# Handing Incoming Messages
# my_dispacher.add_handler()

# Error Handling if any
# my_dispacher.add_error_handler()

# Starting the bot using polling() function and check for messages every sec
updater.start_polling(1.0)
print("Running...")
updater.idle()
