import os
from aiogram import Bot
from aiogram.types import Message
from bot.states import journey_state
from utils import database
from aiogram.fsm.context import FSMContext
from states import register, journey_state
from aiogram.utils.markdown import bold, italic

DATABASE = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)


async def create_journey(message: Message, state: FSMContext):
    await message.answer(
        "Давайте начнем создание путешествия!\nДля начала введите уникальное название"
    )

    await state.set_state(journey_state.JourneyState.journey_name)


async def create_journey_name(message: Message, state: FSMContext):
    await message.answer(f"Отлично! Название путешествия: {bold(message.text)}")
    await message.answer(f"Теперь введите описание путешествия")
    await state.update_data(journeyname=message.text)
    await state.set_state(journey_state.JourneyState.journey_description)


async def create_journey_desciption(message: Message, state: FSMContext):
    await message.answer(f"Превосходно! Описание путешествия: {italic(message.text)}")
    await message.answer(f"Теперь введите количество мест, которые вы желаете посетить")
    await state.update_data(journeyname=message.text)
    await state.set_state(journey_state.JourneyState.jorney_count_locations)


async def count_of_locations(message: Message, state: FSMContext):
    await message.answer(f"Превосходно! Описание путешествия: {italic(message.text)}")
    await message.answer(f"Теперь введите количество мест, которые вы желаете посетить")
    await state.update_data(journeydescription=message.text)
    await state.set_state(journey_state.JourneyState.jorney_count_locations)


async def create_location(message: Message, state: FSMContext):
    await message.answer(f"Количество локаций: {bold(message.text)}")
    await message.answer(
        f"Теперь введите название локации, которую вы бы хотели посетить"
    )
    await state.update_data(journeylocationscount=message.text)
    await state.set_state(journey_state.JourneyState.journey_location)
