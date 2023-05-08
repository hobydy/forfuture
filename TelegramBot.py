import re
from aiogram import Bot, Dispatcher, executor, types
import random
from TOKEN import TOKEN
import emoji
from TgBot.cryptoinfo import mdlltc, mdlbtc, mdleth, btc_price, ltc_price, eth_price

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Обрабатываю команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет {message.from_user.full_name}\n"
                        f"Я умный помошник.\n"
                        f"Включаю в себя некоторые функции.\n"
                        f"Воспользуйся командой /info что увидеть весь список доступнхы функций")


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
        # Если число не найдено, генерируем случайное число от 1 до 100
        await message.reply('Случайное число от 1 до 100:\n' + str(random.randint(1, 100)))


# Обрабатываю команду /info
@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.reply(f"{message.from_user.full_name} данный бот разработан что бы помочь и облегчить пользование 'Telegram'\n"
                        f"Не продавая и Не пропагандируя ничего Не законного.\n"
                        f"Список доступных команд:\n"
                        f"/info - Показывает информацию о боте\n"
                        f"/roll - Генерирует любое случайное число в заданом деапазоне\n"
                        f"/rules - Правила чата Цитадель\n"
                        f"/mdlltc - Пишем команду указав сразу сумму обмена в леях MDL-LTC - '/mdlltc 500'\n"
                        f"/mdlbtc - Пишем команду указав сразу сумму обмена в леях MDL-BTC\n"
                        f"/mdleth - Пишем команду указав сразу сумму обмена в леях MDL-ETH\n"
                        f"/coinprices' - Актуальная цена популярных криптовалют"
                        )


# Обрабатываю команду /rules
@dp.message_handler(commands=['rules'])
async def send_info(message: types.Message):
    await message.reply(f"Строго запрещено в общем чате Цитадели:\n\n"
                        f"{emoji.emojize(':camera_with_flash:')}Скидывать фотографии содержащие порнографию, насилие и фотографии местоположений запрещенных веществ.\n\n"
                        f"{emoji.emojize(':hot_springs:')}Оскорблять администрацию или участников сообщества на не определенной основе /ban.\n\n"
                        f"{emoji.emojize(':cross_mark:')}Обсуждение запрещенных веществ не предусмотренных сообществом.\n\n"
                        f"{emoji.emojize(':double_exclamation_mark:')}Мы не приветствуем людей которые используют несколько аккаунтов для извлечения \n"
                        f"выгоды в проводимых мероприятиях{emoji.emojize(':double_exclamation_mark:')}.")


# Обрабатываю добавление нового пользователя в группу
@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    for user in message.new_chat_members:
        await message.answer(f"Привет, {user.full_name}!{emoji.emojize(':waving_hand:')}\n"
                             f"{emoji.emojize(':castle:')}Добро пожаловать в Цитадель{emoji.emojize(':castle:')}\n"
                             f"{emoji.emojize(':trident_emblem:')}Что бы узнать правила нашего сообщества воспользуйтесь командой /rules{emoji.emojize(':trident_emblem:')}")


# Обрабатываю команду /coinprices
@dp.message_handler(commands=['coinprices'])
async def send_info(message: types.Message):
    await message.reply(f"Цена на BTC на текущий момент: ${str(btc_price)}\n"
                        f"Что бы конвертировать MDL в BTC используй команду /mdlbtc '500'\n\n"
                        f"Цена на LTC на текущий момент: ${str(ltc_price)}\n"
                        f"Что бы конвертировать MDL в LTC используй команду /mdlltc '500'\n\n"
                        f"Цена на ETH на текущий момент: ${str(eth_price)}\n"
                        f"Что бы конвертировать MDL в ETH используй команду /mdleth '500'")


@dp.message_handler(commands=['mdlltc'])
async def convert_mdl(message: types.Message):
    # Извлекаем число из сообщения с помощью регулярного выражения
    match = re.search(r'\d+', message.text)
    if match:
        # Если число найдено, преобразуем его в число с плавающей точкой
        number = float(match.group())
        # Получаем цену в лтк из мдл
        convert = mdlltc * number
        # Конвертируем получиные значения
        await message.reply(f'{number} MDL в LTC будет: {convert} LTC')


@dp.message_handler(commands=['mdlbtc'])
async def convert_mdl(message: types.Message):
    # Извлекаем число из сообщения с помощью регулярного выражения
    match = re.search(r'\d+', message.text)
    if match:
        # Если число найдено, преобразуем его в число с плавающей точкой
        number = float(match.group())
        # Получаем цену в лтк из мдл
        convert = mdlbtc * number
        # Конвертируем получиные значения
        await message.reply(f'{number} MDL в BTC будет: {convert} BTC')


@dp.message_handler(commands=['mdleth'])
async def convert_mdl(message: types.Message):
    # Извлекаем число из сообщения с помощью регулярного выражения
    match = re.search(r'\d+', message.text)
    if match:
        # Если число найдено, преобразуем его в число с плавающей точкой
        number = float(match.group())
        # Получаем цену в лтк из мдл
        convert = mdleth * number
        # Конвертируем получиные значения
        await message.reply(f'{number} MDL в ETH будет: {convert} ETH')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
