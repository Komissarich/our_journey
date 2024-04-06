from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buttons = [
    [
        InlineKeyboardButton(text="Никнейм", callback_data="search1"),
        InlineKeyboardButton(text="Город", callback_data="search2"),
    ],
    [InlineKeyboardButton(text="Страна", callback_data="search3")],
]
inline_kb_full = InlineKeyboardMarkup(inline_keyboard=buttons)
