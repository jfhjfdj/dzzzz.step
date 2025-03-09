import asyncio  #для того чтобы бот работал в асинхроном режиме
from aiogram import Bot, Dispatcher, types  #библиотека для работы с Telegram API .создаёт объект бота, диспетчер, работа с телеграм сообщениями
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton #создания кнопок
from aiogram.filters import Command   # создания кнопок
from aiogram.enums import ParseMode#помогает отслеживать команды
TOKEN = "8091911156:AAHJSrAXhJP7va_zAlZ82l4oC6Kq_0C_o5o" # хранит API-токен

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML) #parse_mode=ParseMode.HTML позволяет форматировать текст
dp = Dispatcher() #обьект который будет упрвлять обработчиками сообщений

@dp.message(Command("start")) #функция start() будет срабатывать, когда пользователь отправляет команду /start
async def start(message: types.Message): #функция, которая принимает объект message
    await message.answer("Привет!") #бот отправляет пользователю сообщение Привет!

@dp.message(Command ("help"))
async def help(message: types.Message):
    await message.answer("Я умею отвечать на команду start")#  бот отвечает: Я умею отвечать на команду start

async def main(): #создаёт главную асинхронную функцию для запуска бота
    await dp.start_polling(bot) #бесконечный цикл, в котором бот ждёт и обрабатывает новые сообщения

if __name__ == "__main__": # проверяет, запущен ли скрипт напрямую
    asyncio.run(main()) # активирует асинхронный режим
    