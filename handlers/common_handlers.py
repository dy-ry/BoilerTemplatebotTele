from telebot.async_telebot import AsyncTeleBot
import logging

# Konfigurasi logging untuk debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def register_handlers(bot: AsyncTeleBot):
    """Mendaftarkan semua handler umum."""

    @bot.message_handler(func=lambda message: True)
    async def echo_message(message):
        """Menangani semua pesan teks dan mengembalikannya sebagai echo."""
        logger.info(f"Echoing message from {message.from_user.id}: {message.text}")
        await bot.reply_to(message, message.text)