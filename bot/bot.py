import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from utils import commands, database
from handlers import (
    start,
    registration,
    show_profile,
    user_search,
    add_friend,
    remove_friend,
    friends,
    change_info,
)
from states import register
from states.search_states import nickname_search, town_search, country_search
from states.change_profile_states import (
    change_nickname,
    change_age,
    change_town,
    change_country,
    change_description,
    change_photo,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
POSTGRES_CONN = os.getenv("POSTGRES_CONN")
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
DATABASE = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)
async def set_commands():
    commands_ = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="help", description="Помощь в работе с ботом"),
        BotCommand(command="profile", description="Посмотреть свой профиль"),
        BotCommand(command="edit_profile", description="Изменить свой профиль"),
        BotCommand(command="user_search", description="Поиск пользователей"),
        BotCommand(command="friends", description="Список друзей"),
        BotCommand(command="new_journey", description="Создать путешествие"),
        BotCommand(command="jorneys", description="Список путешествий"),
    ]

    await bot.set_my_commands(commands_, BotCommandScopeDefault)


async def main() -> None:
    await dp.start_polling(bot)
    await set_commands()


# Хэндлер старта
dp.message.register(start.get_start, Command(commands="start"))

# Хэндлеры регистрации
dp.message.register(
    registration.start_register, F.text == "Зарегистрироваться на сайте"
)
dp.message.register(registration.register_nickname, register.RegisterState.regName)
dp.message.register(registration.register_age, register.RegisterState.regAge)
dp.message.register(registration.register_town, register.RegisterState.regTown)
dp.message.register(registration.register_country, register.RegisterState.regCountry)
dp.message.register(registration.register_descr, register.RegisterState.regDescr)
dp.message.register(registration.register_image, register.RegisterState.regImage)

# Хэндлер своего профиля
dp.message.register(show_profile.show_profile, Command(commands="profile"))


# Хэндлеры поиска
dp.message.register(user_search.search, Command(commands="user_search"))
dp.callback_query.register(user_search.start_by_nickname, F.data == "search1")
dp.message.register(user_search.search_by_nickname, nickname_search.SearchState.nick)
dp.callback_query.register(user_search.start_by_town, F.data == "search2")
dp.message.register(user_search.search_by_town, town_search.SearchState.town)
dp.callback_query.register(user_search.start_by_country, F.data == "search3")
dp.message.register(user_search.search_by_country, country_search.SearchState.country)


# Хэндлер клавиатуры добавления в друзья
@dp.callback_query(lambda c: c.data and c.data.startswith("add_friend"))
async def add_friend_callback(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    message = callback_query.message
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.send_message(callback_query.from_user.id, text="Добавление в друзья")
        await add_friend.add_friend(callback_query.from_user.id, message, bot)


# Хэндлер списка друзей
dp.message.register(friends.show_friends, Command(commands=["friends"]))


# Хэндлер клавиатуры удаления из друзей
@dp.callback_query(lambda c: c.data and c.data.startswith("remove_friend"))
async def remove_friend_callback(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    message = callback_query.message
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.send_message(callback_query.from_user.id, text="Удаление из друзей")
        await remove_friend.remove_friend(callback_query.from_user.id, message, bot)
    elif code == 2:
        await bot.send_message(callback_query.from_user.id, text="Ваши путешествия:")


# Хэндлер создания путешествия


if __name__ == "__main__":
    asyncio.run(main())
