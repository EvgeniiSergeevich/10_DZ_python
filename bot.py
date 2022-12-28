import telebot
import model

bot = telebot.TeleBot("5888397915:AAFE6Y3eScQGDbeU4WLlT8z31wnSpkjFik8")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Для обновления курсов валют, введите /init\n " + 
                "Для поиска конкретной валюты введите название (доллар/евро/usd/EUR и т.п)")

@bot.message_handler(commands=['init'])
def send_init(message):
    model.refresh()
    model.init_dict('daily_json.json')
    bot.send_message(message.chat.id, 'Курсы обновлены!')


@bot.message_handler(content_types='text')
def send_valute(message):
    find = str(message.text)
    if len(model.find_valute(find)) == 0:
        bot.send_message(message.chat.id, 'Нет совпадений! Попробуйте снова!')
    else:
        bot.send_message(message.chat.id, model.find_valute(find))


print("Бот запущен!")

bot.infinity_polling()