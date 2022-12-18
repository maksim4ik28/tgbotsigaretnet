from aiogram import types, executor, Dispatcher, Bot
from aiohttp.client import request
from bs4 import BeautifulSoup
import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot("5760905130:AAHmEMumhBZTfUTPN3PTAWKh9PZBIR3Xozs")
dp = Dispatcher(bot)

b1 = KeyboardButton ('/Aссортимент')
b2 = KeyboardButton ('/Адрес')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2)

# команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, """
Добро пожаловать! Я бот , который покажет тебе товары в  <b><a href="https://www.sigaretnet.by">Sigaret.net</a></b>""",
                           parse_mode="html", disable_web_page_preview=1, reply_markup=kb_client)

peremennay = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='POD',callback_data='parsPOD'),\
                                                   InlineKeyboardButton(text='Жидкости',callback_data='parsJidk'),\
                                                   InlineKeyboardButton(text='Одноразки',callback_data='parsOdn'),\
                                                   InlineKeyboardButton(text='Вейпы',callback_data='parsVeip'),\
                                                   InlineKeyboardButton(text='Уголь для кальяна',callback_data='parsYgol'),\
                                                   InlineKeyboardButton(text='Смеси для кальянов',callback_data='parsCmec'))

@dp.message_handler(commands=['Aссортимент'])
async def button(message: types.Message):
    await message.answer('Ассортимент магазина :',reply_markup=peremennay)


#парсинг
#парсинг подов
@dp.callback_query_handler(text='parsPOD')
async def button_command(callback : types.CallbackQuery):
    url = 'https://www.sigaretnet.by/pod-sistemy/bycreated_on.html?format=html&keyword='
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='spacer product-container')
    for i in data:
        name = i.find('div', class_='h2').text
        price = i.find('div', class_='vm3pr-2').text
        img = 'https://www.sigaretnet.by' + i.find('img',class_='browseProductImage').get('src')
        cilka = 'https://www.sigaretnet.by' + i.find('a').get('href')
        await callback.message.answer_photo(img,
                                            caption=name + "<b>\n" + "Стоимость :  " + "</b>" + price + "  \n" + cilka,
                                            parse_mode="html")
        await callback.answer()
        if data.index(i) == 9:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")
# парсинг жидкостей

@dp.callback_query_handler(text='parsJidk')
async def button_command(callback : types.CallbackQuery):
    url = 'https://www.sigaretnet.by/zhidkosti/bycreated_on.html?format=html&keyword='
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='spacer product-container')
    for i in data:
        name = i.find('div', class_='h2').text
        price = i.find('div', class_='vm3pr-2').text
        img = 'https://www.sigaretnet.by' + i.find('img',class_='browseProductImage').get('src')
        cilka = 'https://www.sigaretnet.by' + i.find('a').get('href')
        await callback.message.answer_photo(img,
                                            caption=name + "<b>\n" + "Стоимость :  " + "</b>" + price + "  \n" + cilka,
                                            parse_mode="html")
        await callback.answer()
        if data.index(i) == 9:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")

# парсинг одноразок

@dp.callback_query_handler(text='parsOdn')
async def button_command(callback : types.CallbackQuery):
    url = 'https://www.sigaretnet.by/katalog/disposables.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='spacer product-container')
    for i in data:
        name = i.find('div', class_='h2').text
        price = i.find('div', class_='vm3pr-2').text
        img = 'https://www.sigaretnet.by' + i.find('img',class_='browseProductImage').get('src')
        cilka = 'https://www.sigaretnet.by' + i.find('a').get('href')
        await callback.message.answer_photo(img,
                                            caption=name + "<b>\n" + "Стоимость :  " + "</b>" + price + "  \n" + cilka,
                                            parse_mode="html")
        await callback.answer()
        if data.index(i) == 9:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")

# парсинг вейпов

@dp.callback_query_handler(text='parsVeip')
async def button_command(callback : types.CallbackQuery):
    url = 'https://www.sigaretnet.by/vejpy.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='spacer product-container')
    for i in data:
        name = i.find('div', class_='h2').text
        price = i.find('div', class_='vm3pr-2').text
        img = 'https://www.sigaretnet.by' + i.find('img',class_='browseProductImage').get('src')
        cilka = 'https://www.sigaretnet.by' + i.find('a').get('href')
        await callback.message.answer_photo(img,
                                            caption=name + "<b>\n" + "Стоимость :  " + "</b>" + price + "  \n" + cilka,
                                            parse_mode="html")
        await callback.answer()
        if data.index(i) == 9:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")

# парсинг уголь для кальянов

@dp.callback_query_handler(text='parsYgol')
async def button_command(callback : types.CallbackQuery):
    url = 'https://www.sigaretnet.by/kalyan/ugol-dlya-kalyana.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='spacer product-container')
    for i in data:
        name = i.find('div', class_='h2').text
        price = i.find('div', class_='vm3pr-2').text
        img = 'https://www.sigaretnet.by' + i.find('img',class_='browseProductImage').get('src')
        cilka = 'https://www.sigaretnet.by' + i.find('a').get('href')
        await callback.message.answer_photo(img,
                                            caption=name + "<b>\n" + "Стоимость :  " + "</b>" + price + "  \n" + cilka,
                                            parse_mode="html")
        await callback.answer()
        if data.index(i) == 9:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")
# парсинг смеси для кальянов
@dp.callback_query_handler(text='parsCmec')
async def button_command(callback : types.CallbackQuery):
    url = 'https://www.sigaretnet.by/kalyan/tabak-smesi.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='spacer product-container')
    for i in data:
        name = i.find('div', class_='h2').text
        price = i.find('div', class_='vm3pr-2').text
        img = 'https://www.sigaretnet.by' + i.find('img',class_='browseProductImage').get('src')
        cilka = 'https://www.sigaretnet.by' + i.find('a').get('href')
        await callback.message.answer_photo(img,
                                            caption=name + "<b>\n" + "Стоимость :  " + "</b>" + price + "  \n" + cilka,
                                            parse_mode="html")
        await callback.answer()
        if data.index(i) == 9:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")

# парсинг адреса магазинов

@dp.message_handler(commands=['Адрес'])
async def parser(message: types.Message):
    url = 'https://www.sigaretnet.by/adresa-magazinov/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='col-12 col-sm-12 col-md-12')
    for i in data:
        name = i.find('div', class_='page-header').text
        price = i.find('div', class_='rezhim-raboty').text
        img = i.find('div',class_='adres').text
        await bot.send_message(message.chat.id, name+"\n"+price+"\n"+img,
                            parse_mode="html")
        if data.index(i) == 43:
            break
    if len(data) == 0:
        await bot.send_message(message.chat.id, "Ничего не найдено")


executor.start_polling(dp)
