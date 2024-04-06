import os
from aiogram import Bot
from aiogram.types import Message
from utils import database
from keyboards import inline_search_kb, inline_add_friend
from aiogram.fsm.context import FSMContext
from states.search_states import nickname_search, town_search, country_search
from aiogram.utils.media_group import MediaGroupBuilder

DATABASE = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)


async def search(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        "Выберите категорию поиска",
        reply_markup=inline_search_kb.inline_kb_full,
    )


async def start_by_nickname(message: Message, state: FSMContext):
    await message.answer("Введите никнейм для поиска")
    await state.set_state(nickname_search.SearchState.nick)


async def search_by_nickname(message: Message, bot: Bot, state: FSMContext):

    nickname = message.text
    profiles = db.search_by_nickname(nickname)
    await message.answer(f"Вы ищете никнейм: {nickname}")
    await message.answer(f"Результатов найдено: {len(profiles)}")
    for profile in profiles:
        name = profile[1]
        age = profile[2]
        town = profile[3]
        country = profile[4]
        description = profile[5]
        image_url = profile[7]
        s = f"Никнейм: {name} \nВозраст {age} \nНаселенный пункт: {town} \nСтрана: {country}  \nО себе: {description} \nФото:"
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=image_url,
            caption=s,
            reply_markup=inline_add_friend.inline_kb_full,
        )
    await state.clear()


async def start_by_town(message: Message, state: FSMContext):
    await message.answer("Введите город для поиска")
    await state.set_state(town_search.SearchState.town)


async def search_by_town(message: Message, bot: Bot, state: FSMContext):
    town = message.text
    profiles = db.search_by_city(town)
    await message.answer(f"Вы ищете город: {town}")
    await message.answer(f"Результатов найдено: {len(profiles)}")
    await state.clear()
    for profile in profiles:
        name = profile[1]
        age = profile[2]
        town = profile[3]
        country = profile[4]
        description = profile[5]
        image_url = profile[7]
        s = f"Никнейм: {name} \nВозраст {age} \nНаселенный пункт: {town} \nСтрана: {country}  \nО себе: {description} \nФото:"
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=image_url,
            caption=s,
            reply_markup=inline_add_friend.inline_kb_full,
        )


async def start_by_country(message: Message, state: FSMContext):
    await message.answer("Введите страну для поиска")
    await state.set_state(country_search.SearchState.country)


async def search_by_country(message: Message, bot: Bot, state: FSMContext):
    country = message.text
    profiles = db.search_by_country(country)
    await message.answer(f"Вы ищете страну: {country}")
    await message.answer(f"Результатов найдено: {len(profiles)}")
    state.clear()
    for profile in profiles:
        name = profile[1]
        age = profile[2]
        town = profile[3]
        country = profile[4]
        description = profile[5]
        image_url = profile[7]
        s = f"Никнейм: {name} \nВозраст {age} \nНаселенный пункт: {town} \nСтрана: {country}  \nО себе: {description} \nФото:"
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=image_url,
            caption=s,
            reply_markup=inline_add_friend.inline_kb_full,
        )
