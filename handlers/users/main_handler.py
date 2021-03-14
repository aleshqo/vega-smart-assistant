import logging
import asyncio

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import menu_callBack
from keyboards.inline.choice_buttons import choice, main_menu_keyboard, want_to_know_more_detail, \
    increase_rate_growth_keyboard, earn_on_an_affiliate_program_keyboard, end_of_first_section_keyboard, \
    commissions_and_taxes_keyboard, terms_keyboard, tariffs_keyboard, end_of_second_section_keyboard, \
    end_of_third_section_keyboard
from loader import dp


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

    await call.message.answer_photo(open('resources/safe_funds.jpg', 'rb'))
    # await asyncio.sleep(1)safe_funds
    await call.message.answer(
        "«Текст #4 "
        "рассказать о преимуществах безопасности хранения средств в нашем проекте 💸"
        "Целевая годовая доходность может быть неогранична»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #5 рассказать о принципиальной схеме хранения USDT 💸»",
                              reply_markup=increase_rate_growth_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="increase_rate_growth"))
async def increase_rate_growth_btn(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")

    await call.message.answer_photo(open('resources/increase_rate.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #6 тезис об основных принципах роста курса в зависимости от транзакций»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #7 Теперь обсудим основные критерии зависимости роста курса моент(токенов)»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #8 1️⃣ Курс монет(токенов) растет от…»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #9 2️⃣ Курс моне(токенов) растет от…»")
    # await asyncio.sleep(1)
    await call.message.answer("«Тут всё, перейдем дальше...»", reply_markup=earn_on_an_affiliate_program_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="earn_on_an_affiliate_program"))
async def earn_on_an_affiliate_program(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")

    await call.message.answer_photo(open('resources/earn_on_an_affiliate_program.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer(
        "«Помимо прямого способа заработать как клиент Партнерская программа помогает создать дополнительный доход, "
        "состоящего из 6️⃣ бонусов» коротко без подробностей перечислить бонусы партнерской программы")
    # await asyncio.sleep(1)
    await call.message.answer("«1️⃣Реферальный бонус 💰 Текст #10 👥 »")
    # await asyncio.sleep(1)
    await call.message.answer("«6️⃣Реферальный бонус 💰 Текст #11 👥 »")
    # await asyncio.sleep(1)
    await call.message.answer("«❗ Внимание❗ "
                              "Прибыль клиентов и партнёров CryptoBank «VEGA» "
                              "не зависит от поступлений новых вложений, "
                              "потому что средства на выплату дохода идут только от Комиссий☝ »")
    # await asyncio.sleep(1)
    await call.message.answer("«Мы создаём лучший инструмент для достижения ваших целей 🎯 » ")
    # await asyncio.sleep(1)
    await call.message.answer("«Вы можете вернуться в меню или подробнее узнать о «Партнерской программе»👇",
                              reply_markup=end_of_first_section_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="back_to_main_menu_from_first"))
async def go_back_to_main_menu(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer("Основное меню:", reply_markup=main_menu_keyboard)


#
#
# participate in ICO
#
#

@dp.callback_query_handler(menu_callBack.filter(button_name="participate_in_ico"))
async def participate_in_ico(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer_photo(open('resources/ico_logo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer(
        "«Текст #12» Коротко цепляем (обозначаем основную проблематику «Гавнокоинов» и потерьв «гавнопроектах»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #13» Короткая подача решения проблемы и сохранение интриги"
                              " «На самом деле благодаря DeFi решение есть! "
                              "Сейчас пришло то Время, когда крипто проекты просто обязаны иметь ликвидность "
                              "для возврата инвестиций если стартап не реализован!»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #14» Коротко рассказать что это DeFi проект. Что он предполагает smart-контракты")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #15» Рассказать почему проект начинается с ICO"
                              " показать преимущество перед уже готовыми проектами")
    # await asyncio.sleep(1)

    await call.message.answer("«Текст #16» (Тут нужна логическая привязка на продолжение в другой кнопке по примеру"
                              " Тут всё, перейдем дальше…)", reply_markup=commissions_and_taxes_keyboard)


#
#
#  taxes
#
#

@dp.callback_query_handler(menu_callBack.filter(button_name="commissions_and_taxes"))
async def commissions_and_taxes(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer_photo(open('resources/comission_logo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #17» Мы заботимся о развитии системы иделаем всё, для ее развития!»"
                              " Добавить еще продающий текст📃")
    # await asyncio.sleep(1)
    await call.message.answer("«Итак, давайте по порядку разберем условия "
                              "которые влияют на рост стоимости монеты (токена):»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #16» (Тут нужна логическая привязка на продолжение в другой кнопке по примеру"
                              " Тут всё, перейдем дальше…)", reply_markup=terms_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="commissions_btn"))
async def commissions(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer_photo(open('resources/comission_logo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Комиссия 1% взимаемая в момент выпуска(эмиссии) новых монет(токенов) в залог под USDT»")
    # await asyncio.sleep(1)
    await call.message.answer("«Комиссия 1% за внутри-сетевые переводы с кошелька на кошелек.»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #18» «Могут быть добавлены комисси по кредитованию»")
    await call.message.answer("«Текст #19» «Все виды комиссий "
                              "которые взымаются непосредственно влияют на рост стоимости монеты (токена)»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #20» «Каждая взымаемая комиссия делится на 3 части:")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #21» «50% идут на увеличение стоимости курса монеты(ткена)»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #22» «38% идут на выплаты по партнерской программе»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #23» «12% формируют резервный фонд для развития и доход компании» ")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #24» «Для гарантированного, "
                              "устойчивого развития системы и сбалансированного участия каждого пользователя "
                              "в этом процессе были внедрены ряд условий👇»", reply_markup=terms_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="terms_btn"))
async def commissions(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer("«Текст #25» «Как правило в ICO участвуют разные категории людей.»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #26» «Крипто-энтузиасты - "
                              "хотят со старта принять участие в развитии нового проекта.»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #27» «Кто-то приходит для того "
                              "чтобы вложиться и выгодно зафиксировать свою прибыль на хайпе.»")
    await call.message.answer("«Текст #28» «Кто-то просто хочет пользоваться платежным инструментом или сервисом»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #29» «Всех их объединяет одно желание - "
                              "желание не прогадать в стоимости как на короткой так и на долгой дистанции»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #30» «Условия внедрены для того "
                              "чтобы каждый из участников мог сбалансированно внести свой вклад в развитие системы»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #31» «Итак давайте ознакомимся с основными условиями:»")
    # await asyncio.sleep(1)
    await call.message.answer("«1️⃣Текст #32» «Количество исходящих транзакций»")
    # await asyncio.sleep(1)
    await call.message.answer("«2️⃣Текст #33» «Количество рефералов»")
    # await asyncio.sleep(1)
    await call.message.answer("«3️⃣Текст #34» «Объем структуры»")
    # await asyncio.sleep(1)
    await call.message.answer("«4️⃣Текст #35» добавить еще условия при необходимости")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #36» «Совокупность этих условий формируют для пользователей тарифы»",
                              reply_markup=tariffs_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="tariffs_btn"))
async def commissions(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer("«Текст #37» «Вся экосистема монеты (токена) завязана на количество транзакций. "
                              "Рост стоимости монеты (токена) напрямую зависит от транзакций»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #38» «Внедрение тарифов позволяет:» ")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #39» «Исключить недобросовестное обогащение одних пользователей («холдеров») "
                              "за счет других («юзеров») которые активно развивают экосистему»")
    await call.message.answer("«Текст #40» «Увеличить количество транзакций» ")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #41» «Справедливым образом сбалансировать соотношение вклада в пул обеспечения "
                              "монеты (токена) между «Холдерами» и «Юзерами»»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #42» «Ускорить формирование Фонда развития»")
    # await asyncio.sleep(1)
    await call.message.answer("«Текст #43» «Более подробную информацию для самостоятельного ознакомления 👇»",
                              reply_markup=end_of_second_section_keyboard)


@dp.callback_query_handler(menu_callBack.filter(button_name="presentation"))
async def commissions(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"user={call.message.chat.username}, callback_data='{callback_data}'")
    await call.message.answer_photo(open('resources/presentation_logo.jpg', 'rb'))
    # await asyncio.sleep(1)
    await call.message.answer("«Здесь вы найдёте презентацию компании👇»")
    # await asyncio.sleep(1)
    await call.message.answer_document(open('resources/presentation.pdf', 'rb'))
    await call.message.answer("«Вы можете вернуться в меню 👇»",
                              reply_markup=end_of_third_section_keyboard)
