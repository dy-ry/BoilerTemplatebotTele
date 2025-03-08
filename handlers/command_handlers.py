from utils.keyboard_utils import create_inline_keyboard, create_simple_keyboard
from telebot.async_telebot import AsyncTeleBot
from handlers.message_handlers import *
import logging

# Konfigurasi logging untuk debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def register_handlers(bot: AsyncTeleBot):
    """Mendaftarkan semua handler perintah khusus."""

    @bot.message_handler(commands=['start', 'help'])
    async def send_welcome(message):
        """Menangani perintah /start dan /help."""
        text = f"{MSG_GREATING['welcome']}, @{message.from_user.username}!"
        # Buat inline keyboard dinamis
        buttons_data = [
            {'text': 'Say Hi', 'callback_data': 'say_hi'},
            {'text': 'Get Info', 'callback_data': 'get_info'},
            {'text': 'Quit', 'callback_data': 'quit'}
        ]
        keyboard = create_inline_keyboard(buttons_data)
        
        logger.info(f"Received /start or /help from {message.from_user.id}")
        # await bot.reply_to(message, text)
        await bot.reply_to(message, text, reply_markup=keyboard)
    
    @bot.message_handler(commands=['test'])  # Contoh perintah lain
    async def test_command(message):
        """Menangani perintah /test dengan button sederhana."""
        username = message.from_user.username or 'Unknown'
        text = f"Operasi: {MSG_OUTPUT['success']}\nPilih opsi:"
        
        # Buat keyboard sederhana
        keyboard = create_simple_keyboard(['Yes', 'No'])
        
        logger.info(f"Received /test from User ID: {message.from_user.id}, Username: @{username}")
        await bot.reply_to(message, text, reply_markup=keyboard)
        
    @bot.callback_query_handler(func=lambda call: True)
    async def handle_callback(call):
        """Menangani semua callback dari inline keyboard."""
        user_id = call.from_user.id
        username = call.from_user.username or 'Unknown'
        callback_data = call.data
        
        logger.info(f"Received callback '{callback_data}' from User ID: {user_id}, Username: @{username}")
        
        if callback_data == 'say_hi':
            await bot.answer_callback_query(call.id, "Hi back!")
            await bot.send_message(call.message.chat.id, f"{MSG_GREATING['other']} from EchoBot!")
        elif callback_data == 'get_info':
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.message.chat.id, "I am EchoBot, here to echo your messages!")
        elif callback_data == 'quit':
            await bot.answer_callback_query(call.id, "Goodbye!")
            await bot.send_message(call.message.chat.id, "Bot stopped. Use /start to begin again.")
        elif callback_data == 'yes':
            await bot.answer_callback_query(call.id, "You chose Yes!")
            await bot.send_message(call.message.chat.id, "Great choice!")
        elif callback_data == 'no':
            await bot.answer_callback_query(call.id, "You chose No!")
            await bot.send_message(call.message.chat.id, "Okay, maybe next time!")
        else:
            await bot.answer_callback_query(call.id, "Unknown command")