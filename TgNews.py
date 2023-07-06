import requests
from bs4 import BeautifulSoup
import telebot
import time
import datetime
from telebot import types



TOKEN = '6246521809:AAENE1U1TkyHs5umrcKRnJexqbV2HsRsbbE' 



bot = telebot.TeleBot(TOKEN)



'---------------------------------------------------------------------------------------------------------------------'



@bot.message_handler(commands=['start'])
def start_message(message):


    
    # Создание клавиатуры
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
    markup.add(*buttons)



    # Отправка сообщения
    bot.send_message(message.chat.id, 'Список последних новостей на сегодня:', reply_markup=markup)
    
    
    
    time.sleep(1)

    # Получение данных с веб-сайта
    url = f'https://kaktus.media/?lable=8&date={datetime.datetime.now().strftime("%Y-%m-%d")}&order=time'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    


    # Парсинг заголовков статей
    articles = soup.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
    headlines = [article.find('a', class_='ArticleItem--name').text for article in articles]



    # Отправка первых 20 заголовков статей
    message_text = ''
    for i, headline in enumerate(headlines[:20], start=1):
        message_text += f'{i}. {headline}\n'
    bot.send_message(message.chat.id, message_text)



    time.sleep(1)



'---------------------------------------------------------------------------------------------------------------------'
# В душе не знаю как нормально спарсить содержимое так, чтобы при выходи новой новости оно обновлялось
# P.S. Сделал, что смог самостоятельно!!!



# Парсинг первых 20 ссылок
url = f'https://kaktus.media/?lable=8&date={datetime.datetime.now().strftime("%Y-%m-%d")}&order=time'
html_code = requests.get(url).text
links = [link.get('href') for link in BeautifulSoup(html_code, 'html.parser').find_all('a', class_ = 'ArticleItem--name')[:20]]



# Репарсинг заголовков, имначе код далее не работает
url = f'https://kaktus.media/?lable=8&date={datetime.datetime.now().strftime("%Y-%m-%d")}&order=time'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
headlines = [article.find('a', class_='ArticleItem--name').text for article in articles]



# Жесть, знаю... но лучше так, чем никак (Все Dеscription разные, все работает)
@bot.message_handler(func=lambda message: True)
def process_message(message):
    if message.text == '1':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Dеscription')
        markup.add(button)
        message_text = headlines[0]
        bot.send_message(message.chat.id, message_text)
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Dеscription':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[0]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '2':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Descriptiоn')
        markup.add(button)
        message_text = headlines[1]
        bot.send_message(message.chat.id, message_text)
        time.sleep(0.5)        
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Descriptiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[1]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '3':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Dеscriptiоn')
        markup.add(button)
        message_text = headlines[2]
        bot.send_message(message.chat.id, message_text)
        time.sleep(0.5)        
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Dеscriptiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[2]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '4':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Desсription')
        markup.add(button)
        message_text = headlines[3]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Desсription':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[3]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '5':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Descriрtion')
        markup.add(button)
        message_text = headlines[4]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Descriрtion':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[4]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '6':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Dеsсription')
        markup.add(button)
        message_text = headlines[5]
        bot.send_message(message.chat.id, message_text)       
        time.sleep(0.5) 
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Dеsсription':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[5]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '7':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Dеscriрtion')
        markup.add(button)
        message_text = headlines[6]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Dеscriрtion':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[6]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '8':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Desсriрtion')
        markup.add(button)
        message_text = headlines[7]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Desсriрtion':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[7]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '9':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Desсriptiоn')
        markup.add(button)
        message_text = headlines[8]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Desсriptiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[8]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '10':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('Descriрtiоn')
        markup.add(button)
        message_text = headlines[9]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'Descriрtiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[9]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '11':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('description')
        markup.add(button)
        message_text = headlines[10]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'description':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[10]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '12':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('dеscription')
        markup.add(button)
        message_text = headlines[11]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'dеscription':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[11]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '13':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('desсription')
        markup.add(button)
        message_text = headlines[12]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'desсription':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[12]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '14':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('descriрtion')
        markup.add(button)
        message_text = headlines[13]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'descriрtion':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[13]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '15':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('descriptiоn')
        markup.add(button)
        message_text = headlines[14]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'descriptiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[14]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '16':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('dеsсription')
        markup.add(button)
        message_text = headlines[15]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'dеsсription':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[15]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '17':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('dеscriрtion')
        markup.add(button)
        message_text = headlines[16]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'dеscriрtion':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[16]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '18':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('dеscriptiоn')
        markup.add(button)
        message_text = headlines[17]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'dеscriptiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[17]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

    elif message.text == '19':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('desсriрtion')
        markup.add(button)
        message_text = headlines[18]
        bot.send_message(message.chat.id, message_text)       
        time.sleep(0.5) 
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'desсriрtion':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[18]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
        
    elif message.text == '20':
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('desсriptiоn')
        markup.add(button)
        message_text = headlines[19]
        bot.send_message(message.chat.id, message_text)        
        time.sleep(0.5)
        text = '*some title news you can see Description of this news and Photo*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    if message.text == 'desсriptiоn':
        bot.send_message(message.chat.id, 'Вот вся известная информация:')
        message_text = links[19]
        bot.send_message(message.chat.id, message_text)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        buttons = [telebot.types.KeyboardButton(str(i)) for i in range(1, 21)]
        markup.add(*buttons)
        text = '*Желаете прочитать о чем-то еще?*'
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    


    elif message.text == '/quit':
        bot.send_message(message.chat.id, 'Досвидания')
        bot.send_sticker (message.chat.id, 'CAACAgIAAxkBAAEJnAVkpnizzO58KbYzBQABWlCYSOBNsyoAApgFAAIjBQ0AAaHPCgFysbMiLwQ')
    


bot.polling()