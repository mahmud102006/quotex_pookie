import random
def extract_pair_from_image(image_path):
    return "EURUSD-OTC"  # এখানে OCR বা AI ইউজ করে ইমেজ থেকে পেয়ার বের করবেন

def generate_signal(pair):
    signal = random.choice(["CALL", "PUT"])
    confidence = random.randint(75, 95)
    trend = "Uptrend" if signal == "CALL" else "Downtrend"
    return signal, confidence, trend

def next_trade_time():
    from datetime import datetime, timedelta
    next_minute = (datetime.utcnow() + timedelta(minutes=1)).replace(second=0, microsecond=0)
    return next_minute.strftime("%H:%M UTC")
