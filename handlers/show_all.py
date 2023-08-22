from aiogram import types, Dispatcher
from create_bot import bot, dp, HandleTextState
from db_records import print_rec
from aiogram.dispatcher import FSMContext


# @dp.message_handler(state=HandleTextState.show_all)
async def get_records_command(message: types.Message, state=FSMContext):
    records = await print_rec()
    for record in records:
        info_str = f"ID: {record['ID']}\nГлава: {record['Chapter']}\nНазвание: {record['Name']}\nДата публикации {record['Date']}\n"
        await bot.send_photo(message.chat.id, record['URL'], caption=info_str)
    await state.finish()


def register_handlers_show_all(dpr: Dispatcher):
    dp.register_message_handler(get_records_command, state=HandleTextState.show_all)
