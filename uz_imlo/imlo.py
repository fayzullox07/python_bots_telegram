# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from main import checkWord


# API_TOKEN = '5054743108:AAHEX8g4uGzzZ7UtsY0ORHhWfplooPk2W3E'


# logging.basicConfig(level=logging.INFO)


# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler(commands='start')
# async def send_welcome(message: types.Message):
#     await message.reply("UZ_Imlo Botiga xush kelibiz!\n\nBotdan foydalinish uchun so'z yuboring.")
#     # await message.reply("Botdan foydalinish uchun so'z yuboring.")
# # @dp.message_handler(commands='start')
# # async def help_user(message: types.Message):


# @dp.message_handler()
# async def checkImlo(message: types.Message):
#     word = message.text
#     result = checkWord(word)    
#     if result['available']:
#         response = f"✅ {word.capitalize()}"
#     else:
#         response = f"❌{word.capitalize()}\n"
#         for text in result['matches']:
#             response += f"✅{text.capitalize()}\n"
#     await message.answer(response)        
    

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)    
    
#     # python imlo.py
    
    
    
    
    
#     # heroku ps:scale worker=1
    
    
    
    
