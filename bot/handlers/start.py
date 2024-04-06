from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard


async def get_start(message: Message, bot: Bot):

    await bot.send_message(
        message.from_user.id,
        f"Привет, {message.from_user.full_name}! Для работы с ботом необходимо зарегистрировать аккаунт",
        reply_markup=register_keyboard,
    )
