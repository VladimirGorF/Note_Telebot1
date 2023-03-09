import re
import sqlite3
import datetime
import telebot
import data_base
import addition_modul
import change_module
import deletion_modul
import search_and_return_module

API_TOKEN = '5936246114:AAGCbe54p6aXYNxWmFa0iaKnh05wosaWSus'
bot = telebot.TeleBot(API_TOKEN)
print('Server started')


@bot.message_handler(commands=['start'])
def help_message(message):
    bot.send_message(message.chat.id, f"Предлагаем вашему вниманию следующий функцонал:\n/showAll\n/search\n/delete\n/change\n/add")

@bot.message_handler(commands=['add'])
def help_message(message):
    bot.send_message(message.chat.id, f"Вносите данные в формате: 'add: title; note; author' ")


@bot.message_handler(commands=['delete'])
def del_message(message):
    bot.send_message(message.chat.id, "Удалите запись используя del: и введя через пробел id записки")


@bot.message_handler(commands=['change'])
def help_message(message):
    bot.send_message(message.chat.id, f"Вносите изменения в формате:  'change: noteid title note author'. Используйте "
                                      f"пробел как разделитель.")


@bot.message_handler(commands=['search'])
def help_message(message):
    bot.send_message(message.chat.id, f"Поиск может быть осуществлен в формате 'OR'- когда результатом будет "
                                      f"информация содержащая в себе любой элемент запроса или в формате 'FULL' - когда "
                                      f"результатом будет только полное совпадение параметров запроса в одной записи.  "
                                      f"Вводите search_or: или search_full: затем через 1 пробел аргументы поиска.  ")


@bot.message_handler(commands=['showAll'])
def showAll(message):
    conn = sqlite3.connect('notes.db', check_same_thread=False)
    cur = conn.cursor()
    all_results = search_and_return_module.search_all()
    bot.send_message(message.chat.id, "Полная база данных:")
    for i in all_results:
        bot.send_message(message.chat.id, f' {i}')
    bot.send_message(message.chat.id,
                     f"Чего желаете:\n/showAll\n/search\n/delete\n/change\n/add")

@bot.message_handler(content_types='text')
def search_and_change(message):
    conn = sqlite3.connect('notes.db', check_same_thread=False)
    cur = conn.cursor()
    text = message.text
    text = re.split(' ', text)
    if text[0] == 'change:':
        text.remove(text[0])
        change_module.sql_update(text)
        bot.send_message(message.chat.id, 'Запись изменена!')
    elif text[0] == 'search_or:':
        text.remove(text[0])
        bot.send_message(message.chat.id, 'Идет поиск, подождите...')
        res = search_and_return_module.search_or(text)
        bot.send_message(message.chat.id, f'Мы нашли для Вас:')
        for i in res:
            bot.send_message(message.chat.id, f'{i}')
    elif text[0] == 'search_full:':
        text.remove(text[0])
        bot.send_message(message.chat.id, 'Идет поиск, подождите...')
        res = search_and_return_module.search_full(text)
        bot.send_message(message.chat.id, f'Мы нашли полное совпадение:')
        for i in res:
            bot.send_message(message.chat.id, f'{i}')
    elif text[0] == 'del:':
        text.remove(text[0])
        bot.send_message(message.chat.id, 'Идет удаление, подождите...')
        res = deletion_modul.del_note(text[0])  # удаляем по id
        bot.send_message(message.chat.id, f'Запись удалена!')
    elif text[0] == 'add:':
        text.remove(text[0])
        bot.send_message(message.chat.id, 'Идет добавление, подождите...')
        res = addition_modul.add_note(text)
        bot.send_message(message.chat.id, f'Запись добавлена!')

    bot.send_message(message.chat.id,
                     f"Чего желаете:\n/showAll\n/search\n/delete\n/change\n/add")


bot.polling()

#finish