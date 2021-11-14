import telebot
#Важный коментарий
bot = telebot.TeleBot('1655026971:AAE5-t08Tdvqv9-3pXXuL8EFV5_INvxZnzc')


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привет!":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "Кто ты?:)":
        bot.send_message(message.from_user.id, "Я тестовый чатбот для учебного примера")
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.from_user.id, "Меня зовут MyFirstTestBot.")
    elif message.text == "Сколько тебе лет?":
        bot.send_message(message.from_user.id, "Мне лень отвечать")
    else:
        bot.send_message(message.from_user.id, "Эээээ... Что? Я не понимаю((((")


bot.polling(none_stop=True, interval=0)
