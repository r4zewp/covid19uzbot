from aiogram import *
from pymongo import *

def kb_sub_gen(lang):
    kb_sub = types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(text = eval("sub_y" + f"{lang}"), callback_data = "y"),
        types.InlineKeyboardButton(text = eval("sub_n" + f"{lang}"), callback_data = "n"),
    )

def get_users(db):
    users = list(db.users.find({}))
    ids = []
    for user in users:
        ids.append(user["user_id"])
    return ids
