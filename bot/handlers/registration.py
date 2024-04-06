import os
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import register
from utils import database

DATABASE = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
db = database.Database(DATABASE, POSTGRES_USER, POSTGRES_PASSWORD)


async def start_register(message: Message, state: FSMContext):
    # if db.check_registered(message.from_user.id) is True:
    #     await state.clear()
    #     await message.answer(
    #         "Вы уже зарегистрированы, но вы можете поменять информацию о себе с помощью /profile",
    #     )
    # else:
    await message.answer(
        "Давайте начнем регистрацию \nДля начала укажите ваш никнейм, под которым вас увидят другие пользователи",
    )
    await state.set_state(register.RegisterState.regName)


async def register_nickname(message: Message, state: FSMContext):
    if db.check_nickname(message.text) is True:
        await message.answer(f"Такой никнейм уже занят! Выберите другой")
    else:
        await message.answer(
            f"Приятно познакомиться {message.text}. \nТеперь укажите ваш возраст"
        )
        await state.update_data(regname=message.text)
        await state.set_state(register.RegisterState.regAge)


async def register_age(message: Message, state: FSMContext):
    try:
        int(message.text)
    except Exception:
        await message.answer("Некорректный возраст")
    await message.answer(f"Ваш возраст: {message.text}. \nТеперь укажите ваш город")
    await state.update_data(regage=message.text)
    await state.set_state(register.RegisterState.regTown)


async def register_town(message: Message, state: FSMContext):
    await message.answer(f"Ваш город: {message.text}. \nТеперь укажите вашу страну")
    await state.update_data(regtown=message.text)
    await state.set_state(register.RegisterState.regCountry)


async def register_country(message: Message, state: FSMContext):
    await message.answer(f"Ваш страна: {message.text}. \nМожете написать о себе")
    await state.update_data(regcountry=message.text)
    await state.set_state(register.RegisterState.regDescr)


async def register_descr(message: Message, state: FSMContext):
    await message.answer(f"О себе: {message.text}. \nТеперь отправьте фото для профиля")
    await state.update_data(regdescr=message.text)
    await state.set_state(register.RegisterState.regImage)


async def register_image(
    message: Message,
    state: FSMContext,
    bot: Bot,
):
    await state.update_data(regimage=message.photo[0].file_id)
    reg_data = await state.get_data()
    reg_name = reg_data.get("regname")
    reg_age = reg_data.get("regage")
    reg_town = reg_data.get("regtown")
    reg_descr = reg_data.get("regdescr")
    reg_country = reg_data.get("regcountry")
    reg_image_url = reg_data.get("regimage")
    await message.answer(
        f"Никнейм: {reg_name} \n Возраст {reg_age} \n Населенный пункт: {reg_town} \n Страна: {reg_country}  \n О себе: {reg_descr} \n Фото:",
    )
    await bot.send_photo(chat_id=message.from_user.id, photo=reg_image_url)
    await message.answer(
        "Поздравляем, аккаунт создан, вы сможете изменить данные в дальнейшем"
    )
    db.create_user(
        reg_name,
        reg_age,
        reg_town,
        reg_country,
        reg_descr,
        reg_image_url,
        message.from_user.id,
    )
    await state.clear()
