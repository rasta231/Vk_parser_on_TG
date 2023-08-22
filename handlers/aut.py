from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from create_bot import bot, dp, HandleTextState


# @dp.message_handler(state=HandleTextState.waiting_for_login)
async def log_in(message: types.Message, state: FSMContext):
    user_login = message.text
    await message.answer('Введите пароль')
    await HandleTextState.waiting_for_password.set()
    async with state.proxy() as data:
        data['login'] = user_login


# @dp.message_handler(state=HandleTextState.waiting_for_password)
async def pas_in(message: types.Message, state: FSMContext):
    user_pas = message.text
    async with state.proxy() as data:
        user_login = data['login']
        data['pas'] = user_pas
    await message.answer(f"Логин: {user_login}, Пароль: {user_pas}")
    await state.finish()


def register_handlers_aut(dpr: Dispatcher):
    dp.register_message_handler(log_in, state=HandleTextState.waiting_for_login)
    dp.register_message_handler(pas_in, state=HandleTextState.waiting_for_password)
