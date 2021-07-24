from aiogram import *
from functions import *
from pymongo import *
from config.config import *
from config.kb import *
from json import *

database_client = MongoClient(f"mongodb+srv://{MONGO_DB_LOGIN}:{MONGO_DB_PASSWORD}@cluster0.jkmj6.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority")
db = database_client.users


########## /start
async def start(message: types.Message):
    ids = get_users(db)
    if not(message.from_user.id in ids):
        await message.answer(text = "*Добро пожаловать!*\n\nВыберите язык использования:", \
        parse_mode = types.ParseMode.MARKDOWN, reply_markup = kb_lang)
    else:
        info = await get_today_info()
        await message.answer(text = f"*Статистика по коронавирусу за сегодня:*\n\nСегодня заболело: {info['todayCases']}\nСегодня смертей: {info['todayDeaths']}\
    \nСегодня восстановились: {info['todayRecovered']}", \
            parse_mode = types.ParseMode.MARKDOWN)

########## callback-ru
async def callback_ru(message: types.Message):
    user_list = list(db.users.find({}))
    users_id = []
    for each in user_list:
        users_id.append(each["user_id"])
    if not (message.from_user.id in users_id):
        db.users.insert_one({"user_id": message.from_user.id, "lang": "ru"})
        kb_sub = kb_sub_gen("ru")
        await message.message.answer(text = "Бот может присылать Вам ежедневную статистику по ситуации в стране.\n\n*Подписаться на обновления?*", \
            reply_markup = kb_sub, parse_mode = types.ParseMode.MARKDOWN)
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
        kb_sub = kb_sub_gen("uz")
        await message.message.answer(text = "Bot sizga mamlakatdagi vaziyat bo'yicha har kungi statistik ma'lumotlarni yuborishi mumkin.\n\n*Obuna bo'lasizmi?*", \
            reply_markup = kb_sub, parse_mode = types.ParseMode.MARKDOWN)
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
        kb_sub = kb_sub_gen("en")
        await message.message.answer(text = "Bot can send you updated COVID-19 statistics every day.\n\n*Do you want to subscribe?*", \
            reply_markup = kb_sub, parse_mode = types.ParseMode.MARKDOWN)
    else: 
        db.users.find_one_and_update({"user_id": message.from_user.id}, {"$set": {"lang": "en"}})
        await message.message.answer(text = "*You successfully changed language to English.*", parse_mode = types.ParseMode.MARKDOWN)

####### callback yes

async def callback_yes(message: types.Message):
    db.users.find_one_and_update({'user_id': message.from_user.id}, {"$set": {"sub": "yes"}})
    user = list(db.users.find({"user_id": message.from_user.id}))
    lang = user[0]["lang"]
    info = await get_today_info()
    await message.message.answer(text = eval("success_" + f"{lang}"), parse_mode = types.ParseMode.MARKDOWN)
    await message.message.answer(text = f"*Статистика по коронавирусу за сегодня:*\n\nСегодня заболело: {info['todayCases']}\nСегодня смертей: {info['todayDeaths']}\
    \nСегодня восстановились: {info['todayRecovered']}", \
            parse_mode = types.ParseMode.MARKDOWN)
    
####### callback no

async def callback_no(message: types.Message):
    await message.answer(text = "Ну и пошел нахуй")