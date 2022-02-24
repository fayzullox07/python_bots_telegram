# import logging
# from aiogram import Bot, Dispatcher, executor, types
# import requests
# # from pprint import pprint as print

# API_TOKEN = '5093088206:AAGSlpSwolZkL-_TY9qu6yaLuFnbDy7xOD4'


# logging.basicConfig(level=logging.INFO)


# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# # API_KEY = "926a8da20e2660ff470413bb"

# # currency = "USD"
# # url = f"https://v6.exchangerate-api.com/v6/{API_TOKEN}/pair/{currency}/UZS"





# @dp.message_handler(commands='start')
# async def send_welcome(message: types.Message):
#     await message.reply("Dollar kursini aniqlab beradigan botga xush kelibsiz!!!\nBotdan foydalanish uchun valyutani tanlang")

# # response = requests.get(urldsd)


# # jsondata = response.json()
# # course = response.json()['conversion_rate']
# # print(f"Bugungi kurs: 1AQSH dollar = {course} so'm")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)    
    