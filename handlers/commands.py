from aiogram import *
from functions import *
from pymongo import *
from config.config import *
from config.kb import *

database_client = MongoClient(f"mongodb+srv://{MONGO_DB_LOGIN}:{MONGO_DB_PASSWORD}@cluster0.jkmj6.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority")
db = database_client.users


########## /start
async def start(message: types.Message):
    ids = get_users(db)
    if not(message.from_user.id in ids):
        await message.answer(text = "*Добро пожаловать!*\n\nВыберите язык использования:", \
        parse_mode = types.ParseMode.MARKDOWN, reply_markup = kb_lang)
    else:
        await message.answer(text = "*Статистика по коронавирусу за сегодня:*", \
            parse_mode = types.ParseMode.MARKDOWN)

########## callback-ru
async def callback_ru(message: types.Message):
    user_list = list(db.users.find({}))
    users_id = []
    for each in user_list:
        users_id.append(each["user_id"])
    if not (message.from_user.id in users_id):
        db.users.insert_one({"user_id": message.from_user.id, "lang": "ru"})
    else: 
        db.users.find_one_and_update({"user_id": message.from_user.id}, {"$set": {"lang": "ru"}})
        await message.message.answer(text = "*Вы успешно изменили язык на русский.*", parse_mode = types.ParseMode.MARKDOWN)

########## callback-uz
async def callback_uz(message: types.Message):
    user_list = db.users.find({})
    users_id = []
    for each in user_list:
        users_id.append(each["user_id"])
    if not (message.from_user.id in users_id):
        db.users.insert_one({"user_id": message.from_user.id, "lang": "uz"})
    else: 
        db.users.find_one_and_update({"user_id": message.from_user.id}, {"$set": {"lang": "uz"}})
        await message.message.answer(text = "*Siz o'z tilingizni muvaffaqiyatli o'zbek tiliga o'zgartirdingiz*", parse_mode = types.ParseMode.MARKDOWN)
        

########## callback-en
async def callback_en(message: types.Message):
    user_list = list(db.users.find({}))
    users_id = []
    for each in user_list:
        users_id.append(each["user_id"])
    if not (message.from_user.id in users_id):
        db.users.insert_one({"user_id": message.from_user.id, "lang": "en"})
    else: 
        db.users.find_one_and_update({"user_id": message.from_user.id}, {"$set": {"lang": "en"}})
        await message.message.answer(text = "*You successfully changed language to English.*", parse_mode = types.ParseMode.MARKDOWN)
    