import os
from flask import Flask, request
from telegram import Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return 'ok'

def start(update, context):
    keyboard = [
        ['Фразы — Звонок'],
        ['Фразы — Торг'],
        ['Фразы — Документы']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Выбери категорию:", reply_markup=reply_markup)

def handle_text(update, context):
    text = update.message.text
    if text == 'Фразы — Звонок':
        update.message.reply_text("📞 Call phrases:\n- Hi, I’m calling about the load...\n- Is it still available?")
    elif text == 'Фразы — Торг':
        update.message.reply_text("💬 Bargaining phrases:\n- Can you do $2400?\n- My driver wants more.")
    elif text == 'Фразы — Документы':
        update.message.reply_text("📄 Document phrases:\n- Please send the rate confirmation.\n- Our MC is 104104.")
    else:
        update.message.reply_text("Выбери одну из кнопок выше.")

dp = Dispatcher(bot, None, workers=0, use_context=True)
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
