from aiogram import Bot,Dispatcher,types,executor
import markups
import logging
import requests
# from aiogram.types import BufferedInputFile
# from aiogram.types import FSInputFile
print("Salom Fayzullo")
# print("Salom Fayzullo")





logging.basicConfig(level=logging.INFO)

token='5138778076:AAHkA3iihZntp7Qwenyg-aKuMtmpSbctTg4'
bot=Bot(token=token)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def first_mesage(message: types.Message):
    await message.reply("Bu bot yordamida rasm ustida turli xil ishlar amallar bajaringiz mumkin ! \n Quyidagilar bizning xizmatlarimiz: ", reply_markup=markups.btn)


@dp.message_handler(content_types=['text'])
async def get_value(message: types.Message):
    r = message.text
    if r == 'Rasm fonini olib tashlash':
        await message.reply("Bu xizmatdan foydalanish uchun fonini olib tashlanishi kerak bo'lgan rasmni bizga jo'nating")

@dp.message_handler(content_types=['photo'])
async def get_photo(message):
    photo = message.photo
    await message.photo[-1].download("images/test.png")

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('images/test.png', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'H5rMinfQu6yopa7mwsYR7iqU'},
    )

    if response.status_code == requests.codes.ok:
        with open('images/out.png', 'wb') as out:
            out.write(response.content)

    else:
        print("Error:", response.status_code, response.text)

    photo_id = out.photo_id
    print(photo_id)
    send_img = open("images/out.png", "r").get_file
    await bot.send_photo(message.from_user.id, send_img, caption="Отправленное фото")
    await bot.send_photo(photo_id, caption="Tayyor")
    






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  