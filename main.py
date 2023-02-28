# 1) Поправить импорты ctrl+o
# 2) Убрать хардкоды путей до файлов
# 3) Поправит БД. Посомтри CREATE OR IGNORE или типа того. Вообще вынести фнукцию из функции. Создавать бд в начале скрипта, а не при каждом вызове.
# 4) Разобраться, почему переводчик кидает ошибку на сервер
# 5) Как закончишь - спросить Костю про tmux
# 6) Поцелдовать Костю. Минет обязательно.

import os
import re
import sqlite3
import ffmpeg
import numpy as np
import pymorphy3
import requests
import speech_recognition as sr
import telebot
import torch
import yaml
from googletrans import Translator
from telebot import types

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

morph = pymorphy3.MorphAnalyzer()

CREDENRIALS_FILE = 'gs_credentials.json'
spreadsheet_id = '10K4UCiuZgLzt-Pwvpgaeq4CriKWoI0Aelqg4p0diaj4'
spreadsheet_id1 = '1Kvckd52v-BOSfhrRKArnE6lZCfZshZoqufwFfDVOEhg'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENRIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)

with open('latest_silero_models.yml', 'r', encoding="utf8") as yaml_file:
    models = yaml.load(yaml_file, Loader=yaml.SafeLoader)
model_conf = models.get('te_models').get('latest')

# see avaiable languages
available_languages = list(model_conf.get('languages'))
print(f'Available languages {available_languages}')

# and punctuation marks
available_punct = list(model_conf.get('punct'))
print(f'Available punctuation marks {available_punct}')

bot_token = '6040925657:AAErLyj7OVgOlqgmxF8npbt5-1aHP9zj6gc'
bot = telebot.TeleBot(bot_token)

def add_to_google_s(id, name, user_name, grade='-'):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="A1:D200",
        valueInputOption="RAW",
        body={
            'values': [
                [id, name, user_name, grade]]
        }).execute()
def google_5(grade='5'):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id1,
        range="A1:A100",
        valueInputOption="RAW",
        body={
            'values': [
                [grade]]
        }).execute()
def google_4(grade='4'):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id1,
        range="A1:A100",
        valueInputOption="RAW",
        body={
            'values': [
                [grade]]
        }).execute()
def google_3(grade='3'):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id1,
        range="A1:A100",
        valueInputOption="RAW",
        body={
            'values': [
                [grade]]
        }).execute()
def google_2(grade='2'):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id1,
        range="A1:A100",
        valueInputOption="RAW",
        body={
            'values': [
                [grade]]
        }).execute()
# def create_table(): #создаю таблицу, если такой не существует
#     connection = sqlite3.connect('bot_data.db')
#     sqlite_create_table_query = ''' CREATE TABLE IF NOT EXISTS user (
#                                     id INTEGER PRIMARY KEY,
#                                     name TEXT NOT NULL,
#                                     user_name text NOT NULL UNIQUE);'''
#     cursor = connection.cursor()
#     print("База данных подключена к SQLite")
#     cursor.execute(sqlite_create_table_query)
#     connection.close()
# create_table()
# def insert_varible_into_table(id, name, user_name):
#     connection = sqlite3.connect('bot_data.db')
#     cursor = connection.cursor()
#     sqlite_insert_with_param = """INSERT INTO user
#                                   (id, name, user_name)
#                                   VALUES (?, ?, ?);"""
#
#     data_tuple = (id, name, user_name)
#     cursor.execute(sqlite_insert_with_param, data_tuple)
#     connection.commit()
#     print("Переменные Python успешно вставлены в таблицу user")
#     connection.close()
@bot.callback_query_handler(lambda callback_query: callback_query.data == "asd")
def voice2text(callback_query):
    chat_id = callback_query.message.chat.id
    bot.send_message(chat_id, "Чтобы я перевел ГС в текстовое сообщение, ты можешь👇 \n\nа) *Записать мне ГС сам*. \nб) *Переслать чье-то ГС мне* -- только не пиши к нему текст, иначе я не сработаю. \n\nЯ отправлю тебе результат спустся 5-15 секунд, зависит от объема. Если ГС будет очень большое - я вышлю тебе *краткое содержание* после транскрибирования в текст🥰", parse_mode="Markdown")
@bot.callback_query_handler(lambda callback_query: callback_query.data == "asdf")
def survey(callback_query):
    chat_id = callback_query.message.chat.id
    markup = types.InlineKeyboardMarkup()  # создали  кнопку
    markup.add(types.InlineKeyboardButton('Супер!', callback_data='super'))
    markup.add(types.InlineKeyboardButton('Хорошо!', callback_data='good'))
    markup.add(types.InlineKeyboardButton('Нормально!', callback_data='normal'))
    markup.add(types.InlineKeyboardButton('Бывало и лучше!', callback_data='nu_takoe'))

    bot.send_message(chat_id, "Оцени, нсколько я тебя был полезен, пожалуйста:", reply_markup=markup, parse_mode="Markdown")
@bot.callback_query_handler(lambda callback_query: callback_query.data == "super")
def grade_1(callback_query):
    chat_id = callback_query.message.chat.id
    bot.send_message(chat_id,'Спасибо за оценку! Уверен, ты поможешь мне стать лучше)')
    google_5()
@bot.callback_query_handler(lambda callback_query: callback_query.data == "good")
def grade_2(callback_query):
    chat_id = callback_query.message.chat.id
    bot.send_message(chat_id,'Спасибо за оценку! Уверен, ты поможешь мне стать лучше)')
    google_4()
@bot.callback_query_handler(lambda callback_query: callback_query.data == "normal")
def grade_3(callback_query):
    chat_id = callback_query.message.chat.id
    bot.send_message(chat_id,'Спасибо за оценку! Уверен, ты поможешь мне стать лучше)')
    google_3()
@bot.callback_query_handler(lambda callback_query: callback_query.data == "nu_takoe")
def grade_4(callback_query):
    chat_id = callback_query.message.chat.id
    bot.send_message(chat_id,'Спасибо за оценку! Уверен, ты поможешь мне стать лучше)')
    google_2()

@bot.callback_query_handler(lambda callback_query: callback_query.data == "as")
def text_translator(callback_query):
    chat_id = callback_query.message.chat.id
    bot.send_message(chat_id, "Я умею переводить текст *с любого языка на Русский* и *с Английского на Русский*. \n\nОтправь мне *текстовое* сообщение, которое необходимо перевести, я сам определю язык🥰", parse_mode="Markdown")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup() #создали  кнопку
    markup.add(types.InlineKeyboardButton('Перевод ГС в текст', callback_data='asd'))
    markup.add(types.InlineKeyboardButton('Переводчик', callback_data='as'))
    bot.reply_to(message, f"Привет, {message.from_user.first_name}!👋 \nМеня зовут Galina-bot, я могу тебе помочь с: \n\n1️⃣ *Переводом* \nУмею переводить с любого языка на Русский или с Русского на Английский.\n\n2️⃣ *Переводом речи в текст*\nАля бесплатный 🔥Telegram Premium🔥\n\n3️⃣ *Кратким пересказом ГС*\nДелаю автоматически, если твоё ГС более 3 предложений.\n\nЧтобы начать мной пользоваться выбери, что тебе нужно👇", reply_markup=markup, parse_mode="Markdown",)
    add_to_google_s(message.from_user.id, message.from_user.first_name, message.from_user.username)
    # insert_varible_into_table(message.from_user.id, message.from_user.first_name, message.from_user.username)

def audio_to_text(dest_name: str):
# Функция для перевода аудио, в формате ".vaw" в текст
    r = sr.Recognizer()
    # тут мы читаем наш .vaw файл
    message = sr.AudioFile(dest_name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language="ru_RU") # используя возможности библиотеки распознаем текст, так же тут можно изменять язык распознавания
    return result

def punctuation(input_text):
    model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir="snakers4/silero-models", source="github", model='silero_te')
    return apply_te(input_text, lan='ru')

@bot.message_handler(content_types = ['text'])
def translate_message(message):
    translator = Translator()
    result = translator.translate(text=message.text)
    if result.src == 'en':
        markup = types.InlineKeyboardMarkup()  # создали  кнопку
        markup.add(types.InlineKeyboardButton('Оценить бота', callback_data='asdf'))
        trans = translator.translate(message.text, dest='ru')
        bot.send_message(message.from_user.id, f'Перевод сообщения с {trans.src} на {trans.dest}: \n*{trans.text}* \n\nНажми на кнопку, чтобы оценить мои способности🙏🏻\n*Это анонимно!*',
                         reply_markup=markup, parse_mode="Markdown")
    else:
        markup = types.InlineKeyboardMarkup()  # создали  кнопку
        markup.add(types.InlineKeyboardButton('Оценить бота', callback_data='asdf'))
        trans = translator.translate(message.text, dest='en')
        bot.send_message(message.from_user.id, f'Перевод сообщения с {trans.src} на {trans.dest}: \n*{trans.text}* \n\nНажми на кнопку, чтобы оценить мои способности🙏🏻\n*Это анонимно!*', reply_markup=markup, parse_mode="Markdown")


@bot.message_handler(content_types = ['voice'])
def get_voice_message(message):
    file_info = bot.get_file(message.voice.file_id)
    path = os.path.splitext(file_info.file_path)[0]  #путь до файла
    fname = os.path.basename(path)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(bot_token, file_info.file_path))
    with open(fname + '.oga', 'wb') as f:
    # with open('voice.ogg', 'wb') as f:
    #     f.write(file.content)
    # subprocess.run(['ffmpeg', '-i', fname + '.oga', fname + '.wav'])
    # subprocess.run(['ffmpeg', '-i', fname + '.oga', fname + '.wav'])  # здесь используется страшное ПО ffmpeg, для конвертации .oga в .vaw
        f.write(file.content)
    # Пизда какой костыль - привязано к конкретному пути до исполянемого файла ffmpeg
    # a = subprocess.run([r"C:\FFmpeg\bin\ffmpeg.exe", '-i', fname + '.oga', fname + '.wav'])  # здесь используется страшное ПО ffmpeg, для конвертации .oga в .vaw

    # sf.read(fname + '.ogg')
    # sf.write(fname + '.wav')

    ffmpeg.input(fname + '.oga').output(fname + '.wav').run()
    result = audio_to_text(fname + '.wav')  # Вызов функции для перевода аудио в текст
    result = result.lower()
    answer = punctuation(result)
    bot.send_message(message.from_user.id, format(answer))
    os.remove(fname + '.wav') #удаляем аудиофайл, чтобы не хранить в папке

    text = answer

    sentences = re.split(r'[\.\!\?]', text)
    sentences = list(map(lambda x: x + ".", sentences))
    clean_text = text.lower()
    clean_text = re.sub(r"[^А-Я^а-я^0-9^ ]", '', clean_text)
    word_tokenize = clean_text.split()

    # стоп-слова рус яз
    stop_words = ["а", "е", "и", "ж", "м", "о", "на", "не", "ни", "об", "но", "он", "мне", "мои", "мож", "она", "они",
                  "оно", "мной", "много", "многочисленное", "многочисленная", "многочисленные", "многочисленный",
                  "мною", "мой", "мог", "могут", "можно", "может", "можхо", "мор", "моя", "моё", "мочь", "над", "нее",
                  "оба", "нам", "нем", "нами", "ними", "мимо", "немного", "одной", "одного", "менее", "однажды",
                  "однако", "меня", "нему", "меньше", "ней", "наверху", "него", "ниже", "мало", "надо", "один",
                  "одиннадцать", "одиннадцатый", "назад", "наиболее", "недавно", "миллионов", "недалеко", "между",
                  "низко", "меля", "нельзя", "нибудь", "непрерывно", "наконец", "никогда", "никуда", "нас", "наш",
                  "нет", "нею", "неё", "них", "мира", "наша", "наше", "наши", "ничего", "начала", "нередко",
                  "несколько", "обычно", "опять", "около", "мы", "ну", "нх", "от", "отовсюду", "особенно", "нужно",
                  "очень", "отсюда", "в", "во", "вон", "вниз", "внизу", "вокруг", "вот", "восемнадцать",
                  "восемнадцатый", "восемь", "восьмой", "вверх", "вам", "вами", "важное", "важная", "важные", "важный",
                  "вдали", "везде", "ведь", "вас", "ваш", "ваша", "ваше", "ваши", "впрочем", "весь", "вдруг", "вы",
                  "все", "второй", "всем", "всеми", "времени", "время", "всему", "всего", "всегда", "всех", "всею",
                  "всю", "вся", "всё", "всюду", "г", "год", "говорил", "говорит", "года", "году", "где", "да", "ее",
                  "за", "из", "ли", "же", "им", "до", "по", "ими", "под", "иногда", "довольно", "именно", "долго",
                  "позже", "более", "должно", "пожалуйста", "значит", "иметь", "больше", "пока", "ему", "имя", "пор",
                  "пора", "потом", "потому", "после", "почему", "почти", "посреди", "ей", "два", "две", "двенадцать",
                  "двенадцатый", "двадцать", "двадцатый", "двух", "его", "дел", "или", "без", "день", "занят", "занята",
                  "занято", "заняты", "действительно", "давно", "девятнадцать", "девятнадцатый", "девять", "девятый",
                  "даже", "алло", "жизнь", "далеко", "близко", "здесь", "дальше", "для", "лет", "зато", "даром",
                  "первый", "перед", "затем", "зачем", "лишь", "десять", "десятый", "ею", "её", "их", "бы", "еще",
                  "при", "был", "про", "процентов", "против", "просто", "бывает", "бывь", "если", "люди", "была",
                  "были", "было", "будем", "будет", "будете", "будешь", "прекрасно", "буду", "будь", "будто", "будут",
                  "ещё", "пятнадцать", "пятнадцатый", "друго", "другое", "другой", "другие", "другая", "других", "есть",
                  "пять", "быть", "лучше", "пятый", "к", "ком", "конечно", "кому", "кого", "когда", "которой",
                  "которого", "которая", "которые", "который", "которых", "кем", "каждое", "каждая", "каждые", "каждый",
                  "кажется", "как", "какой", "какая", "кто", "кроме", "куда", "кругом", "с", "т", "у", "я", "та", "те",
                  "уж", "со", "то", "том", "снова", "тому", "совсем", "того", "тогда", "тоже", "собой", "тобой",
                  "собою", "тобою", "сначала", "только", "уметь", "тот", "тою", "хорошо", "хотеть", "хочешь", "хоть",
                  "хотя", "свое", "свои", "твой", "своей", "своего", "своих", "свою", "твоя", "твоё", "раз", "уже",
                  "сам", "там", "тем", "чем", "сама", "сами", "теми", "само", "рано", "самом", "самому", "самой",
                  "самого", "семнадцать", "семнадцатый", "самим", "самими", "самих", "саму", "семь", "чему", "раньше",
                  "сейчас", "чего", "сегодня", "себе", "тебе", "сеаой", "человек", "разве", "теперь", "себя", "тебя",
                  "седьмой", "спасибо", "слишком", "так", "такое", "такой", "такие", "также", "такая", "сих", "тех",
                  "чаще", "четвертый", "через", "часто", "шестой", "шестнадцать", "шестнадцатый", "шесть", "четыре",
                  "четырнадцать", "четырнадцатый", "сколько", "сказал", "сказала", "сказать", "ту", "ты", "три", "эта",
                  "эти", "что", "это", "чтоб", "этом", "этому", "этой", "этого", "чтобы", "этот", "стал", "туда",
                  "этим", "этими", "рядом", "тринадцать", "тринадцатый", "этих", "третий", "тут", "эту", "суть", "чуть",
                  "тысяч"]
    word2count = {}
    for word in word_tokenize:
        # word = str
        word = morph.parse(word)[0].normal_form
        if word not in stop_words:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1
    print(word2count)

    # взвешенная гистограмма
    for key in word2count.keys():
        word2count[key] = word2count[key] / max(
            word2count.values())  # насколько частовстречается данное слово, относительно САМОГ7О частовстречаемого

    sent2score = {}
    for i, sentence in enumerate(sentences):
        if len(sentence.split(' ')) < 28 and len(sentence.split(' ')) > 6:
            if sentence not in sent2score.keys():
                sent2score[sentence] = 0
            for word in sentence.split():
                if word in word2count.keys():
                    sent2score[sentence] += word2count[
                        word]  # сумма рейтингов слов в конкретном предложении, получили рейтинг предложения
    if len(sent2score) < 4:
        markup = types.InlineKeyboardMarkup()  # создали  кнопку
        markup.add(types.InlineKeyboardButton('Оценить бота', callback_data='asdf'))
        bot.send_message(message.from_user.id, 'Нажми на кнопку, чтобы оценить мои способности🙏🏻\n*Это анонимно!*', reply_markup=markup, parse_mode="Markdown")
        return
    idx = np.flip(
        np.argsort(list(sent2score.values())))  # индексы "рейтингов" предложений по убыванию рейтингов (не индексов!!!)
    best_three_sentences = np.array(list(sent2score.keys()))[idx][:3]
    summary_mes = ''.join(best_three_sentences)
    markup = types.InlineKeyboardMarkup()  # создали  кнопку
    markup.add(types.InlineKeyboardButton('Оценить бота', callback_data='asdf'))
    bot.send_message(message.from_user.id, f'*Краткий пересказ голосового сообщения:*\n{summary_mes}\n\nНажми на кнопку, чтобы оценить мои способности🙏🏻\n*Это анонимно!*', reply_markup=markup, parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)