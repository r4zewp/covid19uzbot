from aiogram import *
from pymongo import *
import requests
from config.phrases import *
from requests import *
from config.config import *

def kb_sub_gen(lang):
    kb_sub = types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(text = eval("sub_y_" + f"{lang}"), callback_data = "y"),
        types.InlineKeyboardButton(text = eval("sub_n_" + f"{lang}"), callback_data = "n"),
    )
    return kb_sub

def get_users(db):
    users = list(db.users.find({}))
    ids = []
    for user in users:
        ids.append(user["user_id"])
    return ids

async def get_today_info():
    info = request("GET", COVID_API).json()
    return info
