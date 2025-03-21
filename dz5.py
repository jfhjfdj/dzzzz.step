import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

TOKEN = "7943338125:AAFANT1ik_WrYWo5I21f2dVQdec2Q7zMe_g"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Начать"), KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Рандомное число")]
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="start")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")],
        [InlineKeyboardButton(text="Рандомное число", callback_data="random")],
    ]
)

@dp.callback_query(F.data.in_({"start", "help", "random"}))
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "start":
        await callback.message.answer("Привет! Я тестовый бот <b>test</b>", reply_markup=main_keyboard)
    elif callback.data == "help":
        await callback.message.answer(
            "<b>Доступные команды:</b>\n/start - Начать работу с ботом\n/help - Список команд\n/random - Случайное число"
        )
    elif callback.data == "random":
        number = random.randint(1, 100)
        await callback.message.answer(f"Случайное число: {number}")
    await callback.answer()  # Чтобы Telegram не думал, что кнопка зависла


@dp.message(Command(commands="start"))
async def start(message: types.Message):
    await message.answer("Привет! Я тестовый бот <b>test</b>", reply_markup=main_keyboard)

@dp.message(Command(commands="random"))
async def random_command(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f"Случайное число: {number}")

@dp.message(Command(commands="help"))
async def help_command(message: types.Message):
    command_text = (
        "<b>Доступные команды:</b>\n"
        "/start - Начать работу с ботом\n"
        "/help - Список команд\n"
        "/random - Случайное число"
    )
    await message.answer(command_text)

@dp.message(F.text == "Начать")
async def start_button(message: types.Message):
    await start(message)

@dp.message(F.text == "Помощь")
async def help_button(message: types.Message):
    await help_command(message)

@dp.message(F.text == "Рандомное число")
async def random_button(message: types.Message):
    await random_command(message)

async def main():
    await dp.run_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
