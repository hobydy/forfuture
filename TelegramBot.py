import re
from aiogram import Bot, Dispatcher, executor, types
import random

TOKEN = "5817389777:AAHRyNVwYVxIs1oyYC0cbKPSH-mMKkCuoxw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Обрабатываю команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ рандом бот\n")

# Обрабатываю команду /roll
@dp.message_handler(commands=['roll'])
async def roll_dice(message: types.Message):
    # Извлекаем число из сообщения с помощью регулярного выражения
    match = re.search(r'\d+', message.text)
    if match:
        # Если число найдено, преобразуем его в целое число
        number = int(match.group())
        # Генерируем случайное число в диапазоне от 1 до number и отправляем его пользователю
        await message.reply(str(random.randint(1, number)))
    else:
        # Если число не найдено, отправляем сообщение об ошибке
        await message.reply(str(random.randint(1, 100)))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
