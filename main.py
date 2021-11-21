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
    data = await s.get_data()

    resp = ''

    for key, value in data.items():
        resp += '<b>{}</b>, {}\n'.format(key, value)

    await call.message.answer(resp)
    await call.answer(text="Спасибо за ответ", show_alert=False)


executor.start_polling(dp, skip_updates=True)
