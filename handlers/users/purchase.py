import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_buttons import choice, pear_keyboard, apples_keyboard, apples_keyboards
from loader import dp, bot

@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Выберите аниме",
                         reply_markup=choice)
@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call:CallbackQuery):
    await call.answer(cache_time=60)

    callback_data=call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Баскетбол",
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="Бездомный бог"))
async def buying_apples(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Бездомный бог",
                              reply_markup=apples_keyboards)

@dp.callback_query_handler(buy_callback.filter(item_name="Воллейбол"))
async def buying_apples(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Воллейбол",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="Завтра"))
async def buying_apples(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Завтра",
                              reply_markup=apples_keyboards)


@dp.callback_query_handler(text = "cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Чтобы смотреть офлайн загрузите на смартфон или ПК", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)