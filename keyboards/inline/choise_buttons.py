from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_BASKETBALL, URL_VOLIBALL, URL_ZAVTRA, URL_BOG
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Баскетбол", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Бездомный богг", callback_data="Бездомный богг:5")
choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Воллейбол", callback_data="buy:Воллейбол:5")
choice.insert(buy_apples)

buy_appless = InlineKeyboardButton(text="Завтра", callback_data="buy:Завтра:5")
choice.insert(buy_appless)

cancel_button = InlineKeyboardButton(text="Назад", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="смотреть", url=URL_BASKETBALL)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="смотреть", url=URL_BOG)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="смотреть", url=URL_VOLIBALL)
    ]
])
apples_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="смотреть", url=URL_ZAVTRA)
    ]
])