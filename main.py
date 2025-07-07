import os
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")

def start(update, context):
    update.message.reply_text("Hello! Bot is working ✅")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()


BOT_PIN = os.getenv("BOT_PIN", "1739")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Rage Sniper Bot! 🔥")

if __name__ == '__main__':
    try:
        print("🔍 TELEGRAM_BOT_TOKEN:", os.getenv("TELEGRAM_BOT_TOKEN"))
        print("🔍 BOT_PIN:", BOT_PIN)
import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)

        app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
    except Exception as e:
        print("❌ CRITICAL ERROR:", e)
