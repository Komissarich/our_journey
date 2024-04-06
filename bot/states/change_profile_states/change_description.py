from aiogram.fsm.state import StatesGroup, State


class ChangeState(StatesGroup):
    description = State()
