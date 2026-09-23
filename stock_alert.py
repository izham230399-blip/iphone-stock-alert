import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.apple.com/my/shop/buy-iphone/iphone-18-pro/6.9-inch-display-512gb-burgundy"

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1"
}

r = requests.get(URL, headers=headers, timeout=30)
r.raise_for_status()

text = BeautifulSoup(r.text, "html.parser").get_text(" ", strip=True)

# Perkataan yang biasanya menunjukkan produk belum boleh dibeli
unavailable_words = [
    "Currently unavailable",
    "Not Available",
    "Unavailable"
]

available = not any(word.lower() in text.lower() for word in unavailable_words)

if available:
    message = (
        "🚨🔥 STOK IPHONE 18 PRO MAX ADA! 🔥🚨\n\n"
        "📱 18 Pro Max\n"
        "💾 512GB\n"
        "🎨 Burgundy\n\n"
        "👉 BUKA SEKARANG:\n"
        f"{URL}"
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )
