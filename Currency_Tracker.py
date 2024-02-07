import requests
from flask import Flask, request
from telegram import Bot
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters
import os

# Your Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.environ.get('5057371942:AAH1dnXAfUT57dzOLo3AObN28lTYCoUutXY')  # Remember to set your token as an environment variable

# Currency symbols and their corresponding API codes
CURRENCIES = {
    "USD": "usd",
    "EUR": "eur",
    "INR": "inr"
}

# API endpoint for currency exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

# Store last fetched exchange rates
last_exchange_rates = {}

# Flask app
app = Flask(__name__)

# Initialize Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)


# Function to get currency exchange rates from the API
def get_exchange_rates(currency):
    response = requests.get(API_URL.format(currency))
    if response.status_code == 200:
        return response.json().get("rates")
    return None


# Function to send notification
def send_notification(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)


# Function to handle the /start command
def start(update, context):
    update.message.reply_text("Currency exchange rate tracking bot is active!")


# Function to handle the /track command
def track(update, context):
    chat_id = update.message.chat_id
    message = "Tracking currency exchange rates:\n"

    for currency, code in CURRENCIES.items():
        rates = get_exchange_rates(code)
        if rates:
            message += f"{currency}: {rates[currency]}\n"
            last_exchange_rates[currency] = rates[currency]
        else:
            message += f"Failed to fetch {currency} exchange rate.\n"

    update.message.reply_text(message)


# Function to check for changes in exchange rates and send notifications
def check_exchange_rates():
    for currency, code in CURRENCIES.items():
        rates = get_exchange_rates(code)
        if rates:
            if currency in last_exchange_rates and last_exchange_rates[currency] != rates[currency]:
                send_notification(os.environ.get('5057371942'), f"{currency} exchange rate has changed!\n"
                                                                     f"New rate: {rates[currency]}")
                last_exchange_rates[currency] = rates[currency]
        else:
            send_notification(os.environ.get('5057371942'), f"Failed to fetch {currency} exchange rate.")


# Endpoint for receiving updates from Telegram
@app.route('/' + TELEGRAM_BOT_TOKEN, methods=['POST'])
def webhook():
    update = request.json
    dispatcher.process_update(update)
    return '', 200


# Error handler
def error(update, context):
    print(f"Update {update} caused error {context.error}")


if __name__ == '__main__':
    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("track", track))

    # Start webhook
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=PORT)

    # Schedule job to check exchange rates once a day
    check_exchange_rates()
