from aiogram.fsm.state import StatesGroup, State


class ChangeState(StatesGroup):
    photo = State()
