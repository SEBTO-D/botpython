import telebot
from telebot import types
token='5760405967:AAHyGTM2JaA_CX1rikU4zzwKzpHOn0P3GNg'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Сайт', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Расскажи о счётчиках', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Как могу записать на CustDev', callback_data=3))
    bot.send_message(message.chat.id, text="Привет я бот Jetsell, чем я могу быть вам полезен?", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, )
    answer = ''
    if call.data == '1':
        answer = 'https://jetsel.ru'
    elif call.data == '2':
        answer = 'Счётчики поситетелей отоброжат реальное кол-во людей '
    elif call.data == '3':
        answer = 'Записаться можно по ссылке\n https://forms.amocrm.ru/rlrlrcr'

    bot.send_message(call.message.chat.id, answer)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text.lower ()=='сайт':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://jetsel.ru')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт", reply_markup=markup)
    elif message.text.lower()=='счётчики':
        bot.send_message(message.chat.id,'Наши счётчики считаю посителей и отправляют в удобном виде на сервер')
bot.infinity_polling()



