import os
from aiogram import Bot
from aiogram.types import Message
from utils import database


async def add_friend(user_id, message: Message, bot: Bot):

    friend_nickname = message.caption.split("\n")[0].split()[1]
    DATABASE = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)
    db.add_friend(user_id, friend_nickname)

    await message.answer(
        f"{friend_nickname} успешно добавлен в друзья",
    )
