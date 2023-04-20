import re
from aiogram import Bot, Dispatcher, executor, types
import random

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Обрабатываю команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет {message.from_user.full_name}\nЯ умный помошник.\nВключаю в себя несколько функций.\nВоспользуйся командой /info что увидеть весь список доступнхы функций")


# Обрабатываю команду /roll
@dp.message_handler(commands=['roll'])
async def roll_dice(message: types.Message):
    # Извлекаем число из сообщения с помощью регулярного выражения
    match = re.search(r'\d+', message.text)
    if match:
        # Если число найдено, преобразуем его в целое число
        number = int(match.group())
        # Генерируем случайное число в диапазоне от 1 до number и отправляем его пользователю
        await message.reply(f'Случайное число от 1 до {number}:\n' + str(random.randint(1, number)))
    else:
        # Если число не найдено, отправляем сообщение об ошибке
        await message.reply('Случайное число от 1 до 100:\n' + str(random.randint(1, 100)))

# Обрабатываю команду /info
@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.reply(f"{message.from_user.full_name} данный бот разработан что бы помочь и облегчить пользование 'Telegram'\nВсе права пренадлежат hobydy\nОбращайтесь в любоем время по поводу сотрудничества.\n"
                        f"Список доступных команд:\n/start - Запускает бота и показывает приветсвенное сообщение\n/info - Показывает информацию о боте\n/roll - Генерирует любое случайное число в заданом деапазоне\nИсходный код бота вы можете найти тут:\nhttps://github.com/hobydy/forfuture"
                        )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
