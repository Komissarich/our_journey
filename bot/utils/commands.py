from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="help", description="Помощь в работе с ботом"),
        BotCommand(command="profile", description="Посмотреть свой профиль"),
        BotCommand(command="user_search", description="Поиск пользователей"),
        BotCommand(command="friends", description="Список друзей"),
        BotCommand(command="new_journey", description="Создать путешествие"),
        BotCommand(command="jorneys", description="Список путешествий"),
    ]

    await bot.send_my_commands(commands, BotCommandScopeDefault())
