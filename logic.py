from PIL import Image
import pytesseract
import datetime
import random

def extract_pair_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    for line in text.split('\n'):
        if "OTC" in line and "/" in line:
            return line.strip()
    return None

def generate_signal(pair):
    # উদাহরণ হিসেবে ট্রেন্ড & সিগন্যাল জেনারেটর
    trend = random.choice(["⬆️ Uptrend", "⬇️ Downtrend", "➡️ Sideways"])
    confidence = random.randint(80, 95)
    signal = "CALL 🔼" if "Up" in trend else "PUT 🔽"
    return signal, confidence, trend

def next_trade_time():
    now = datetime.datetime.now()
    minute = (now.minute // 2 + 1) * 2
    next_time = now.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(minutes=minute)
    return next_time.strftime("%H:%M")
