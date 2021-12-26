import asyncio

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from messages import *
import service as s
import time

bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher(bot)

my_time = [19, 34]

check_time = True


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


async def take_data_from_meteonova():
    global check_time
    while True:
        time_now = [time.localtime()[3], time.localtime()[4]]
        if my_time == time_now:
            if check_time:
                check_time = False
                await s.save_data()
        else:
            check_time = True


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(take_data_from_meteonova())
    executor.start_polling(dp, skip_updates=True)
