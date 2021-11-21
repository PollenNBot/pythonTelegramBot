from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from messages import *
import service as s

bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=GET_WEATHER, callback_data="get_data"))
    await message.answer(START_MESSAGE, reply_markup=keyboard)

@dp.callback_query_handler(text="get_data")
async def buttonAnswer(call: types.CallbackQuery):
    data = await s.get_data()

    resp = ''

    for key, value in data.items():
        resp += '<b>{}</b>, {}\n'.format(key, value)

    await call.message.answer(resp)
    await call.answer(text=CALLBACK_ANSWER, show_alert=False)


executor.start_polling(dp, skip_updates=True)
