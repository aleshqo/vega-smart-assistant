import logging
import asyncio

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import menu_callBack
from keyboards.inline.choice_buttons import choice, main_menu_keyboard, want_to_know_more_detail, \
    increase_rate_growth_btn
from loader import dp, vega_assistant


@dp.message_handler(Command("start"))
async def start_chat(message: Message):
    await message.answer_photo(open('resources/hello_logo.jpg', 'rb'))
    # await asyncio.sleep(0.5)
    await message.answer("Я умный помощник и подробно расскажу Вам о CryptoBank «VEGA»")
    # await asyncio.sleep(1.5)
    await message.answer("«Сейчас внизу появится основное меню. Вы можете выбрать интересующий "
                         "вопрос, нажмите на него и получите развернутый ответ 👍»")
    # await asyncio.sleep(2.5)
    await message.answer("«Вот кнопка основного меню 👇»",
                         reply_markup=choice)


@dp.callback_query_handler(menu_callBack.filter(button_name="menu"))
async def show_menu_buttons(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer("Основное меню:", reply_markup=main_menu_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="about_project"))
async def click_about_project(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")

    await call.message.answer_photo(open('resources/vega_logo.png', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #1»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #2»")
    # await asyncio.sleep(1)
    await call.message.answer("«Вот команда создателей компании 👇»")
    # await asyncio.sleep(1)
    await call.message.answer_photo(open('resources/ceo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Сооснователь и CEO проекта»")
    # await asyncio.sleep(1)
    await call.message.answer_photo(open('resources/founder_ceo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Сооснователь и руководитель команды продвижения»")
    # await asyncio.sleep(1)
    await call.message.answer_photo(open('resources/main_manager.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Сооснователь и руководитель технической команды»")
    # await asyncio.sleep(1)
    await call.message.answer_photo(open('resources/tech_lead_logo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Приглашенный эксперт по продажам»")
    # await asyncio.sleep(1)
    await call.message.answer_photo(open('resources/seller_expert_logo.png', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Теперь я расскажу о том, чем CryptoBank «VEGA» может быть полезен для каждого👍»")
    # await asyncio.sleep(1)
    await call.message.answer("«1️⃣ Став клиентом CryptoBank «VEGA» Выможете безопасно сберечь ваши средства»")
    # await asyncio.sleep(1)
    await call.message.answer("«2️⃣ Вы можете гарантированно приумножить свои средства на росте курса монет(токенов)»")
    # await asyncio.sleep(1)
    await call.message.answer("«3️⃣ Вы можете зарабатывать на партнёрской программе, создавая свою клиентскую базу»")
    # await asyncio.sleep(1)
    await call.message.answer("«4️⃣ Текст #3»")
    # await asyncio.sleep(1)
    # await call.message.answer("«Про что вы хотите узнать подробнее? 👇»")
    # await asyncio.sleep(1)
    await call.message.answer("«Про что вы хотите узнать подробнее? 👇»", reply_markup=want_to_know_more_detail)


@dp.callback_query_handler(menu_callBack.filter(button_name="safely_safeguard_your_funds"))
async def safely_safeguard_your_funds(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")

    await call.message.answer_photo(open('resources/safe_funds.jpeg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer(
        "«Текст #4 "
        "рассказать о преимуществах безопасности хранения средств в нашем проекте 💸"
        "Целевая годовая доходность может быть неогранична»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #5 рассказать о принципиальной схеме хранения USDT 💸»")
    await call.message.answer('Гарантированно приумножить рост курса', reply_markup=increase_rate_growth_btn)

# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "pear"
# @dp.callback_query_handler(text_contains="pear")
# async def buying_pear(call: CallbackQuery):
#     # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
#     # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
#     await call.answer(cache_time=60)
#
#     callback_data = call.data
#
#     # Отобразим что у нас лежит в callback_data
#     # logging.info(f"callback_data='{callback_data}'")
#     # В Python 3.8 можно так, если у вас ошибка, то сделайте предыдущим способом!
#     logging.info(f"{callback_data=}")
#
#     await call.message.answer("Вы выбрали купить грушу. Груша всего одна. Спасибо.",
#                               reply_markup=pear_keyboard)


# Попробуем использовать фильтр от CallbackData
# @dp.callback_query_handler(buy_callback.filter(item_name="apple"))
# async def buying_apples(call: CallbackQuery, callback_data: dict):
#     await call.answer(cache_time=60)
#
#     # Выведем callback_data и тут, чтобы сравнить с предыдущим вариантом.
#     logging.info(f"{callback_data=}")
#
#     quantity = callback_data.get("quantity")
#     await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо.",
#                               reply_markup=apples_keyboard)


# @dp.callback_query_handler(text="cancel")
# async def cancel_buying(call: CallbackQuery):
#     # Ответим в окошке с уведомлением!
#     await call.answer("Вы отменили эту покупку!", show_alert=True)
#
#     # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
#     await call.message.edit_reply_markup(reply_markup=None)

# Вариант 2 отправки клавиатуры (по API)
# await bot.edit_message_reply_markup(chat_id=call.from_user.id,
#                                     message_id=call.message.message_id,
#                                     reply_markup=None)
