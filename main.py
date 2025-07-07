from flask import Flask, request
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

def start(update, context):
    update.message.reply_text("Welcome to Rage Sniper Bot! 🔥")

def signals(update, context):
    update.message.reply_text("🚀 Signal received. Stay sharp.")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("signals", signals))

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Rage Sniper Bot is live!"

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
