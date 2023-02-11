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
        message = "Hello and welcome!\nPlease select a cryptocurrency 🪙:"

    else:
        message = "Please select a cryptocurrency 🪙:"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=ReplyKeyboardMarkup(buttons))


def select_timeframe(update, context):
    buttons = [
        [KeyboardButton(timeframe[0])], 
        [KeyboardButton(timeframe[1])], 
        [KeyboardButton(timeframe[2])], 
        [KeyboardButton(timeframe[3])], 
        [KeyboardButton(timeframe[4])], 
        [KeyboardButton(timeframe[5])], 
        [KeyboardButton(timeframe[6])], 
        [KeyboardButton(timeframe[7])], 
        [KeyboardButton(timeframe[8])], 
        [KeyboardButton(timeframe[9])], 
        ]

    message = "Please select a timeframe ⌛:"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=ReplyKeyboardMarkup(buttons))


def start_function(update, context):
    main_menu(True, update, context)


def message_handler_function(update, context):
    received_message = update.message.text

    if received_message in coin:
        selected_symbol = ""

        for i in range(len(coin)):
            if received_message == coin[i]:
                selected_symbol = coin_symbol[i]

        select_timeframe(update, context)
        
        # handler = TA_Handler(
        #     symbol = selected_symbol,
        #     exchange = "BINANCE",
        #     screener = "crypto",
        #     interval = "1m"
        # )
        
        # analysis = handler.get_analysis()
        # opening = analysis.indicators["open"]
        # closing = analysis.indicators["close"]
        # lowest = analysis.indicators["low"]
        # highest = analysis.indicators["high"]



        # context.bot.send_message(chat_id=update.effective_chat.id, text=output)

    elif received_message in timeframe:
        selected_timeframe = ""

        for i in range(len(timeframe)):
            if received_message == timeframe[i]:
                selected_timeframe = time_symbol[i]
                print(selected_timeframe)


def error_handler_function(update, context):
    print(f"Update: {update} caused error: {context.error}")

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

coin_symbol = [
    "BTCUSD",
    "ETHUSD",
    "USDTUSD",
    "BNBUSD",
    "USDCUSD",
    "XRPUSD",
    "BUSDUSD",
    "ADAUSD",
    "DOGEUSD",
    "SOLUSD"
]

timeframe = [
    "1 Minute",
    "5 Minutes",
    "15 Minutes",
    "30 Minutes",
    "1 Hour",
    "2 Hours",
    "4 Hours",
    "1 Day",
    "1 Week",
    "1 Month"
]

time_symbol = [
    "1m",
    "5m",
    "15m",
    "30m",
    "1h",
    "2h",
    "4h",
    "1d",
    "1W",
    "1M"
]

# Connecting our app with the Telegram API Key and using the context
updater = Updater(token, use_context=True)
my_dispatcher = updater.dispatcher

# Adding CommandHandler from telegram.ext to handle defined functions/commands
my_dispatcher.add_handler(CommandHandler("start", start_function))

# Handing Incoming Messages
my_dispatcher.add_handler(MessageHandler(Filters.text, message_handler_function))

# Error Handling if any
my_dispatcher.add_error_handler(error_handler_function)

# Starting the bot using polling() function and check for messages every sec
updater.start_polling(1.0)
print("Running...")
updater.idle()
