from telebot import TeleBot, types
bot = TeleBot('')

@bot.message_handler(content_types=['text'])
def print_hi(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
