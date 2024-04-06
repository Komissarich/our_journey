from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buttons = [
    [
        InlineKeyboardButton(text="Удалить из друзей", callback_data="remove_friend1"),
        InlineKeyboardButton(
            text="Добавить в путешествие", callback_data="remove_friend2"
        ),
    ]
]
inline_kb_full = InlineKeyboardMarkup(inline_keyboard=buttons)
