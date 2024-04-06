from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buttons = [
    [
        InlineKeyboardButton(text="Никнейм", callback_data="change_info1"),
        InlineKeyboardButton(text="Возраст", callback_data="change_info2"),
    ],
    [
        InlineKeyboardButton(text="Город", callback_data="change_info3"),
        InlineKeyboardButton(text="Страна", callback_data="change_info4"),
    ],
    [
        InlineKeyboardButton(text="О себе", callback_data="change_info5"),
        InlineKeyboardButton(text="Фото", callback_data="change_info6"),
    ],
]
inline_kb_full = InlineKeyboardMarkup(inline_keyboard=buttons)
