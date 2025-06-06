from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import os
from logic import extract_pair_from_image, generate_signal, next_trade_time
import logging

TOKEN = os.environ.get("BOTTOKEN")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("👋 বট চালু হয়েছে! আপনি এখন স্ক্রিনশট পাঠাতে পারেন।")

def handle_photo(update, context):
    photo = update.message.photo[-1].get_file()
    photo_path = "screenshot.jpg"
    photo.download(photo_path)

    pair = extract_pair_from_image(photo_path)
    if pair:
        signal, confidence, trend = generate_signal(pair)
        trade_time = next_trade_time()
        response = f"""
📊 Pair: <b>{pair}</b>
📈 Signal: <b>{signal}</b>
📉 Trend: <b>{trend}</b>
🕒 Trade Time: <b>{trade_time}</b>
🔍 Confidence: <b>{confidence}%</b>
"""
    else:
        response = "❌ Pair খুঁজে পাওয়া যায়নি। অনুগ্রহ করে পরিষ্কার স্ক্রিনশট পাঠান।"

    update.message.reply_text(response, parse_mode=ParseMode.HTML)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
