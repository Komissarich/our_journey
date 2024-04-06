from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buttons = [
    [InlineKeyboardButton(text="Добавить в друзья", callback_data="add_friend1")]
]


inline_kb_full = InlineKeyboardMarkup(inline_keyboard=buttons)
