import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = "9100885514:AAHZeZlMQdDJycqHJKeNJvbhXud1VEJjg3E"
MY_TELEGRAM_ID = 8488756952

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_TELEGRAM_ID:
        return
    await update.message.reply_text("Caw. Le bot est en ligne et prêt à recevoir.")

# --- FAUX SERVEUR WEB POUR RENDER ---
def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), BaseHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    # Lance le faux serveur web en arrière-plan (pour satisfaire Render)
    threading.Thread(target=run_dummy_server, daemon=True).start()
    
    # Lance le bot Telegram
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot en écoute...")
    app.run_polling()