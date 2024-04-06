import os
from aiogram import Bot
from aiogram.types import Message
from utils import database


async def remove_friend(user_id, message: Message, bot: Bot):
    friend_nickname = message.caption.split("\n")[1].split()[1]
    DATABASE = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)
    db.remove_friend(user_id, friend_nickname)

    await message.answer(
        f"{friend_nickname} успешно удален из друзей",
    )
