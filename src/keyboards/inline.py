from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_markup(_):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=_("Subscription"), callback_data="subscription")],
        [InlineKeyboardButton(text=_("Pay"), callback_data="pay")],
        [InlineKeyboardButton(text=_("Get config"), callback_data="config")],
    ])