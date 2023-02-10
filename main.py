from telegram import *
from telegram.ext import *
from tradingview_ta import TA_Handler, Interval, Exchange

from key import token


# start(Boolian): is it a "/start" command or not
def main_menu(start, update, context):
    buttons = [
        [KeyboardButton(coin[0])], 
        [KeyboardButton(coin[1])], 
        [KeyboardButton(coin[2])], 
        [KeyboardButton(coin[3])], 
        [KeyboardButton(coin[4])], 
        [KeyboardButton(coin[5])], 
        [KeyboardButton(coin[6])], 
        [KeyboardButton(coin[7])], 
        [KeyboardButton(coin[8])], 
        [KeyboardButton(coin[9])], 
        ]
    
    if start:
        message = "Hello and welcome!\nPlease choose a cryptocurrency 🪙:"

    else:
        message = "Please choose a cryptocurrency 🪙:"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=ReplyKeyboardMarkup(buttons))


def start_function(update, context):
    main_menu(True, update, context)


def message_handler_function(update, context):
    received_message = update.message.text

    if received_message in coin:
        selected_symbol = ""

        if received_message == coin[0]:
            selected_symbol = "BTCUSD"

        elif received_message == coin[1]:
            selected_symbol = "ETHUSD"

        elif received_message == coin[2]:
            selected_symbol = "USDTUSD"

        elif received_message == coin[3]:
            selected_symbol = "BNBUSD"     

        elif received_message == coin[4]:
            selected_symbol = "USDCUSD"  

        elif received_message == coin[5]:
            selected_symbol = "XRPUSD"  

        elif received_message == coin[6]:
            selected_symbol = "BUSDUSD"  

        elif received_message == coin[7]:
            selected_symbol = "ADAUSD"  

        elif received_message == coin[8]:
            selected_symbol = "DOGEUSD"  

        elif received_message == coin[9]:
            selected_symbol = "SOLUSD"
        
        handler = TA_Handler(
            symbol = selected_symbol,
            exchange = "BINANCE",
            screener = "crypto",
            interval = "1m"
        )
        
        analysis = handler.get_analysis()
        opening = analysis.indicators["open"]
        closing = analysis.indicators["close"]
        lowest = analysis.indicators["low"]
        highest = analysis.indicators["high"]

        # context.bot.send_message(chat_id=update.effective_chat.id, text=output)


coin = [
    "Bitcoin (BTC)",
    "Ethereum (ETH)",
    "Tether (USDT)",
    "Binance Coin (BNB)",
    "U.S. Dollar Coin (USDC)",
    "Ripple (XRP)",
    "Binance USD (BUSD)",
    "Cardano (ADA)",
    "Dogecoin (DOGE)",
    "Solana (SOL)"
]

# Connecting our app with the Telegram API Key and using the context
updater = Updater(token, use_context=True)
my_dispatcher = updater.dispatcher

# Adding CommandHandler from telegram.ext to handle defined functions/commands
my_dispatcher.add_handler(CommandHandler("start", start_function))

# Handing Incoming Messages
my_dispatcher.add_handler(MessageHandler(Filters.text, message_handler_function))

# Error Handling if any
# my_dispacher.add_error_handler()

# Starting the bot using polling() function and check for messages every sec
updater.start_polling(1.0)
print("Running...")
updater.idle()
