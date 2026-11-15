import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = "9100885514:AAHZeZlMQdDJycqHJKeNJvbhXud1VEJjg3E"
MY_TELEGRAM_ID = 8488756952

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_TELEGRAM_ID:
        return
    await update.message.reply_text("Caw. Le bot est en ligne et prêt à recevoir.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot en écoute...")
    app.run_polling()