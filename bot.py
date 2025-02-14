# Boleh recode asal kasih credit gw © HanX

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests
import asyncio

# Ganti Token Bot Lu..
TOKEN = "7747397133:AAHj-JykwhomTQ7zrd1yFHivM4Y2aDZkHqM"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome Sensei..\nTolong kirim saja alamat ip yang ingin dilacak")

async def track_ip(update: Update, context: CallbackContext) -> None:
    ip = update.message.text.strip()

    # Cek apakah format IP valid
    if not ip.replace('.', '').isdigit():
        await update.message.reply_text("Mohon masukkan alamat IP yang benar ya Sensei..")
        return

    # Ambil data lokasi dari IP
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    if data['status'] == 'fail':
        await update.message.reply_text("IP invalid :(")
        return

    # Buat pesan informasi lokasi
    info = (
        f"🔍 Detail IP : {ip}\n"
        f"🌍 Negara : {data['country']} ({data['countryCode']})\n"
        f"🏙 Kota : {data['city']}, {data['regionName']}\n"
        f"📍 Koordinat : {data['lat']}, {data['lon']}\n"
        f"⏰ Zona Waktu : {data['timezone']}\n"
        f"📡 ISP : {data['isp']}\n"
        f"🔗 ORG : {data['org']}\n"
    )

    await update.message.reply_text(info)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_ip))

    print("Bot Online...")
    app.run_polling()

if __name__ == "__main__":
    main()
