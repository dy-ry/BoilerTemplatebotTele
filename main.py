#!/usr/bin/python
import asyncio
import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from handlers.command_handlers import register_handlers as register_command_handlers
from handlers.common_handlers import register_handlers as register_common_handlers

# Muat konfigurasi dari .env
load_dotenv()
token = os.getenv('TELEGRAM_BOT_TOKEN')

# Inisialisasi bot
bot = AsyncTeleBot(token)

# Daftarkan handler dari file terpisah
register_command_handlers(bot)
register_common_handlers(bot)

# Jalankan bot
if __name__ == '__main__':
    asyncio.run(bot.polling())