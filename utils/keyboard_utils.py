# utils/keyboard_utils.py
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Konfigurasi logging untuk debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def create_inline_keyboard(buttons_data):
    """
    Membuat inline keyboard secara dinamis berdasarkan data button yang diberikan.
    
    Args:
        buttons_data (list): List of dict dengan 'text' (teks button) dan 'callback_data' (data callback).
        Contoh: [{'text': 'Yes', 'callback_data': 'yes'}, {'text': 'No', 'callback_data': 'no'}]
    
    Returns:
        InlineKeyboardMarkup: Objek keyboard yang siap digunakan.
    """
    keyboard = InlineKeyboardMarkup()
    
    for button in buttons_data:
        if 'text' not in button or 'callback_data' not in button:
            logger.error("Button data harus memiliki 'text' dan 'callback_data'")
            raise ValueError("Button data harus memiliki 'text' dan 'callback_data'")
        keyboard.add(InlineKeyboardButton(
            text=button['text'],
            callback_data=button['callback_data']
        ))
    
    return keyboard

def create_simple_keyboard(options):
    """
    Membuat inline keyboard sederhana dari list opsi (tanpa callback_data khusus).
    
    Args:
        options (list): List string untuk teks button. Callback data akan sama dengan teks.
                        Contoh: ['Yes', 'No']
    
    Returns:
        InlineKeyboardMarkup: Objek keyboard yang siap digunakan.
    """
    buttons_data = [{'text': option, 'callback_data': option.lower()} for option in options]
    return create_inline_keyboard(buttons_data)