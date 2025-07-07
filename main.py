import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_PIN = os.getenv("BOT_PIN", "1739")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Rage Sniper Bot! 🔥")

if __name__ == '__main__':
    try:
        print("🔍 TELEGRAM_BOT_TOKEN:", os.getenv("TELEGRAM_BOT_TOKEN"))
        print("🔍 BOT_PIN:", BOT_PIN)

        app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
    except Exception as e:
        print("❌ CRITICAL ERROR:", e)