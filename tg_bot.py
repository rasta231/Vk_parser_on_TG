import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from proteckt_info import tg_token
from db_records import db_start, add_record, print_rec

bot = Bot(token=tg_token)
dp = Dispatcher(bot)


async def on_start(_):
    await db_start()


@dp.message_handler(commands=['help', 'start'])
async def command_start(message: types.Message):
    await message.answer('Начало')


@dp.message_handler(commands=['get_records'])
async def get_records_command(message: types.Message):
    records = await print_rec()
    for record in records:
        info_str = f"ID: {record['ID']}\nГлава: {record['Chapter']}\nНазвание: {record['Name']}\nДата публикации {record['Date']}\n"
        await bot.send_photo(message.chat.id, record['URL'], caption=info_str)


executor.start_polling(dp, skip_updates=True, on_startup=on_start)
