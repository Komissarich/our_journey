import os
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards import inline_change_info
from states.change_profile_states import (
    change_nickname,
    change_age,
    change_town,
    change_country,
    change_description,
    change_photo,
)
from utils import database

DATABASE = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)


async def change_info(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        "Выберите то, что хотите изменить",
        reply_markup=inline_change_info.inline_kb_full,
    )


async def start_change_nickname(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Выберите новый никнейм")
    await state.set_state(change_nickname.ChangeState.nickname)


async def edit_nickname(message: Message, state: FSMContext):
    if db.check_nickname(message.text) is True:
        await message.answer(f"Такой никнейм уже занят! Выберите другой")
    else:
        await message.answer(f"Ваш новый никнейм: {message.text}")
        db.update_nickname(message.from_user.id, message.text)
        await state.clear()


async def start_change_age(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Введите возраст")
    await state.set_state(change_age.ChangeState.age)


async def edit_age(message: Message, state: FSMContext):
    try:
        int(message.text)
    except Exception:
        await message.answer("Некорректный возраст")
    await message.answer(f"Возраст: {message.text}")
    db.update_nickname(message.from_user.id, message.text)
    await state.clear()


async def start_change_town(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Выберите новый город")
    await state.set_state(one_command.OneCommandState.input)


async def edit_town(message: Message, state: FSMContext):
    if db.check_nickname(message.text) is True:
        await message.answer(f"Такой никнейм уже занят! Выберите другой")
    else:
        await message.answer(f"Ваш новый никнейм: {message.text}")
        db.update_nickname(message.from_user.id, message.text)
        await state.clear()
