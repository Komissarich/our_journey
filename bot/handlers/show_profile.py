import os
from aiogram import Bot
from aiogram.types import Message
from utils import database
from aiogram.utils.media_group import MediaGroupBuilder


async def show_profile(message: Message, bot: Bot):
    DATABASE = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)
    profile = db.show_profile(message.chat.id)
    name = profile[1]
    age = profile[2]
    town = profile[3]
    country = profile[4]
    description = profile[5]
    image_url = profile[7]
    s = f"Никнейм: {name} \nВозраст {age} \nНаселенный пункт: {town} \nСтрана: {country}  \nО себе: {description} \nФото:"
    await bot.send_photo(chat_id=message.from_user.id, photo=image_url, caption=s)
