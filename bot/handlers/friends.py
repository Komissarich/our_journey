import os
from aiogram import Bot
from aiogram.types import Message
from utils import database
from keyboards import inline_remove_friend


async def show_friends(message: Message, bot: Bot):
    DATABASE = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)
    profiles = db.show_friends(message.from_user.id)
    await bot.send_message(message.from_user.id, "Ваши друзья:")
    n = 0
    for profile in profiles:
        n += 1
        name = profile[1]
        age = profile[2]
        town = profile[3]
        country = profile[4]
        description = profile[5]
        image_url = profile[7]
        s = f"Друг №{n} \nНикнейм: {name} \nВозраст {age} \nНаселенный пункт: {town} \nСтрана: {country}  \nО себе: {description} \nФото:"
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=image_url,
            caption=s,
            reply_markup=inline_remove_friend.inline_kb_full,
        )
