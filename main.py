from bs4 import BeautifulSoup
import requests
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import service as s

bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прогноз", callback_data="get_data"))
    keyboard.add(types.InlineKeyboardButton(text="Нет,на меня", callback_data="button2"))
    await message.answer("Нажми на одну из нас!", reply_markup=keyboard)

@dp.callback_query_handler(text="get_data")
async def buttonAnswer(call: types.CallbackQuery):
    data = await get_data()

    resp = ''

    for key, value in data.items():
        resp += '<b>{}</b>, {}\n'.format(key, value)

    await call.message.answer(resp)
    await call.answer(text="Спасибо за ответ", show_alert=False)


#import telebot
#Важный коментарий
#bot = telebot.TeleBot('1655026971:AAE5-t08Tdvqv9-3pXXuL8EFV5_INvxZnzc')


#@bot.message_handler(content_types=['text'])
#def handle_text_messages(message):
#    if message.text == "Привет!":
#        bot.send_message(message.from_user.id, "Привет")
#    elif message.text == "Кто ты?:)":
#        bot.send_message(message.from_user.id, "Я тестовый чатбот для учебного примера")
#    elif message.text == "Как тебя зовут?":
#        bot.send_message(message.from_user.id, "Меня зовут MyFirstTestBot.")
#    elif message.text == "Сколько тебе лет?":
#        bot.send_message(message.from_user.id, "Мне лень отвечать")
#    else:
#        bot.send_message(message.from_user.id, "Эээээ... Что? Я не понимаю((((")


#bot.polling(none_stop=True, interval=0)
