import  telebot
bot = telebot.TeleBot('5760405967:AAHyGTM2JaA_CX1rikU4zzwKzpHOn0P3GNg');
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()
