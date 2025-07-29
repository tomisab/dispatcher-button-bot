from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Фразы
PHRASES = {
    "👋 Начало разговора": "Hi, I'm calling about the load from Chicago to Atlanta. Is it still available?\n\nПривет, я звоню по поводу груза из Чикаго в Атланту. Он ещё доступен?",
    "💰 Ставка и вес": "What's the rate and the weight?\n\nКакая ставка и вес груза?",
    "🆔 MC и e-mail": "Our MC number is 104104. Please send the rate confirmation to our email.\n\nНаш MC номер 104104. Пожалуйста, отправьте подтверждение ставки на нашу почту.",
    "✅ Завершение": "If you can do 2400, I'll book it now. Thank you!\n\nЕсли вы согласны на 2400, я бронирую. Спасибо!",
}

# Кнопки
BUTTONS = [[key] for key in PHRASES.keys()]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True)
    await update.message.reply_text("Выберите фразу для звонка брокеру 👇", reply_markup=keyboard)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = PHRASES.get(text, "Пожалуйста, выберите фразу из кнопок ниже.")
    await update.message.reply_text(response)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
