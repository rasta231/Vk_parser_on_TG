from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from handlers import reg, aut, show_all
from db_records import db_start
from create_bot import bot, dp, HandleTextState


async def on_start(_):
    await HandleTextState.waiting_for_action.set()
    await db_start()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_login = types.KeyboardButton(text="Вход")
    button_register = types.KeyboardButton(text="Регистрация")
    button_show_all = types.KeyboardButton(text='Вывести все записи')
    keyboard.add(button_login, button_register, button_show_all)

    await message.answer('Для продолжения работы выберите один из вариантов:', reply_markup=keyboard)
    await HandleTextState.waiting_for_action.set()


@dp.message_handler(text=['Вход', 'Регистрация', 'Вывести все записи'], state=HandleTextState.waiting_for_action)
async def choose_action(message: types.Message, state: FSMContext):
    action = message.text
    if action == 'Вход':
        await message.answer('Введите логин', reply_markup=types.ReplyKeyboardRemove())
        await HandleTextState.waiting_for_login.set()
    elif action == 'Регистрация':
        await message.answer('Введите логин:', reply_markup=types.ReplyKeyboardRemove())
        await HandleTextState.reg_log.set()
    elif action == 'Вывести все записи':
        await message.answer('Список всех изменений:', reply_markup=types.ReplyKeyboardRemove())
        await HandleTextState.show_all.set()


if __name__ == "__main__":
    aut.register_handlers_aut(dp)
    reg.register_handlers_reg(dp)
    show_all.register_handlers_show_all(dp)
    executor.start_polling(dp, skip_updates=True)
