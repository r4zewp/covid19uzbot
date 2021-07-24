import logging
from aiogram import *
from config.config import *
from handlers.commands import *
from functions import *

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
mongo_client = MongoClient(f"mongodb+srv://{MONGO_DB_LOGIN}:{MONGO_DB_PASSWORD}@cluster0.jkmj6.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority")
db = mongo_client.users

########## /start
dp.register_message_handler(start, commands = 'start', state = '*')

########## lang callbacks
dp.register_callback_query_handler(callback_ru, lambda call: call.data == "ru")
dp.register_callback_query_handler(callback_uz, lambda call: call.data == "uz")
dp.register_callback_query_handler(callback_en, lambda call: call.data == "en")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)