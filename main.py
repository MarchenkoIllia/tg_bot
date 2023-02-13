import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: message.text=="keyboard")
def echo_message(message):
    # bot.reply_to(message, message.text)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('a')
    itembtn2 = telebot.types.KeyboardButton('v')
    itembtn3 = telebot.types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Input: ", reply_markup=markup)

@bot.message_handler(commands=["help","start"])
def send_welcome(message):
    bot.reply_to(message, "beep")


bot.infinity_polling()
