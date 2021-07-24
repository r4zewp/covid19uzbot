from aiogram import *

kb_lang = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton(text = "\U0001F1FA\U0001F1FF", callback_data = 'uz'),
    types.InlineKeyboardButton(text = "\U0001F1F7\U0001F1FA", callback_data = 'ru'),
    types.InlineKeyboardButton(text = "\U0001F1FA\U0001F1F8", callback_data = 'en')
)