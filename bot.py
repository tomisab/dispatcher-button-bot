from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, Updater

TOKEN = 'ВАШ_ТОКЕН'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

def start(update, context):
    update.message.reply_text("Привет! Я твой бот с кнопками скоро!")

def echo(update, context):
    update.message.reply_text(update.message.text)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

@app.route('/')
def index():
    return 'Бот запущен!'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

if __name__ == '__main__':
    app.run(debug=True)
