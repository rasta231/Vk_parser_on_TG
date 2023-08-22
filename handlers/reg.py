from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import bot, dp, HandleTextState


# @dp.message_handler(state=HandleTextState.reg_log)
async def reg_log_in(message: types.Message, state: FSMContext):
    user_login = message.text
    await message.answer('Введите пароль')
    await HandleTextState.reg_pas.set()
    async with state.proxy() as registr:
        registr['log'] = user_login


# @dp.message_handler(state=HandleTextState.reg_pas)
async def reg_pas_in(message: types.Message, state: FSMContext):
    user_pas = message.text
    async with state.proxy() as registr:
        user_login = registr['log']
        registr['pas'] = user_pas
    await message.answer(f"Логин: {user_login}, Пароль: {user_pas}")
    await state.finish()


def register_handlers_reg(dpr: Dispatcher):
    dp.register_message_handler(reg_log_in, state=HandleTextState.reg_log)
    dp.register_message_handler(reg_pas_in, state=HandleTextState.reg_pas)
