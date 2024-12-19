import telebot
from dotenv import load_dotenv
from os import getenv
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


load_dotenv()


class CryptoSafeBot:
    def __init__(self):
        self.bot = telebot.TeleBot(token=getenv("TOKEN"))

    def start(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            print(message.chat.id, message.chat.username)
            markup = InlineKeyboardMarkup()

            btn_lang_ua = InlineKeyboardButton("🇺🇦UA", callback_data="ua")
            btn_lang_en = InlineKeyboardButton("🇺🇸EN", callback_data="en")
            markup.row(btn_lang_ua, btn_lang_en)

            self.bot.send_message(message.chat.id, "Select language", reply_markup=markup)

        print("Start bot...")
        self.bot.infinity_polling()


if __name__ == '__main__':
    bot = CryptoSafeBot()
    bot.start()
