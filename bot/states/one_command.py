from aiogram.fsm.state import StatesGroup, State


class OneCommandState(StatesGroup):
    input = State()
