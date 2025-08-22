import telebot
from config import API_TOKEN
from logic_ai import get_class

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот который определяет джойстики! Отправь картинку и я расскажу, для какой консоли этот прибор.")
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    class_name, score = get_class(file_name)
    bot.send_message(message.chat.id, class_name)
bot.polling()  