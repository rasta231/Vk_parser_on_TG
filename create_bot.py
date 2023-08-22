from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

from proteckt_info import tg_token

bot = Bot(token=tg_token)
dp = Dispatcher(bot, storage=MemoryStorage())


class HandleTextState(StatesGroup):
    waiting_for_login = State()
    waiting_for_password = State()
    waiting_for_action = State()
    reg_log = State()
    reg_pas = State()
    show_all = State()




