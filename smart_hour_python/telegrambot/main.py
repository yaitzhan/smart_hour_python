"""
Простой echo бот.

Смартчас "Знакомство с Python"

Перед запуском Вам необходимо создать бота в телеграме и скопировать токен в API_TOKEN

"""

import logging

from aiogram import Bot, Dispatcher, executor, types

# скопируйте токен полученный от @BotFather
API_TOKEN = ''

# логгирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Оператор, отслеживающий событие: пользователь ввел `/start`
    """
    # можно поменять текст
    text = "Привет, я простой бот"
    await message.reply(text)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    Оператор, отслеживающий событие: пользователь ввел `/help`
    """
    # можно поменять текст
    text = "Спешу на помощь!"
    await message.reply(text)


@dp.message_handler(regexp='кот')
async def cats(message: types.Message):
    # открывает файл
    with open('data/cat.jpg', 'rb') as photo:
        """
        Напишите боту "кот" и посмотрите что получится
        """
        await message.reply_photo(photo, caption='Not bad 😺')


@dp.message_handler()
async def echo(message: types.Message):
    """
    Простой оператор, который отправляет введенный раннее юзером текст
    """
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
