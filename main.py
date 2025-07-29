import telebot
from flask import Flask, request
import os

TOKEN = os.environ.get('BOT_TOKEN')  # Вставь токен в переменные окружения на Render
bot = telebot.TeleBot(TOKEN)

# === Кнопки ===
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('📞 Позвонить брокеру', '📄 Документы', '📦 Типы грузов')
    bot.send_message(message.chat.id, "Выбери нужный пункт:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def answer(message):
    if message.text == '📞 Позвонить брокеру':
        bot.send_message(message.chat.id, "Hi, I’m calling about the load from Dallas to Chicago. Is it still available?")
    elif message.text == '📄 Документы':
        bot.send_message(message.chat.id, "Rate confirmation, BOL (Bill of Lading), POD (Proof of Delivery)...")
    elif message.text == '📦 Типы грузов':
        bot.send_message(message.chat.id, "Dry Van, Reefer, Flatbed, Step Deck...")
    else:
        bot.send_message(message.chat.id, "Выбери одну из кнопок ниже 👇")

# === Flask сервер для Render ===
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    return "Bot is alive", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
