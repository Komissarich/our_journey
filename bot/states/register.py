from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    regName = State()
    regAge = State()
    regTown = State()
    regCountry = State()
    regDescr = State()
    regImage = State()
