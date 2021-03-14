from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import menu_callBack

# кнопка меню
choice = InlineKeyboardMarkup(row_width=1)
menu_btn = InlineKeyboardButton(text="Меню", callback_data=menu_callBack.new(button_name="menu"))
choice.insert(menu_btn)

# список кнопок главного меню
main_menu_keyboard = InlineKeyboardMarkup(row_width=1)
about_project_btn = InlineKeyboardButton(text="«О проекте CryptoBank «VEGA» 🌐»",
                                         callback_data=menu_callBack.new(button_name="about_project"))
participate_in_ico_btn = InlineKeyboardButton(text="«Участие в ICO 📈»",
                                              callback_data=menu_callBack.new(button_name="participate_in_ico"))

commissions_and_taxes_btn = InlineKeyboardButton(text="«Комиссии, Условия и Тарифы ✍»",
                                                 callback_data=menu_callBack.new(button_name="commissions_and_taxes"))

presentation_btn = InlineKeyboardButton(text="«Презентация 📣»",
                                        callback_data=menu_callBack.new(button_name="presentation"))

partner_program_btn = InlineKeyboardButton(text="«Партнерская программа 🤝»",
                                           callback_data=menu_callBack.new(button_name="partner_program"))

road_map_btn = InlineKeyboardButton(text="«Дорожная карта 📆»",
                                    callback_data=menu_callBack.new(button_name="road_map"))

down_w_paper_btn = InlineKeyboardButton(text="«Скачать White Paper 📄»",
                                        callback_data=menu_callBack.new(button_name="down_w_paper"))

main_menu_links_btn = InlineKeyboardButton(text="«Полезные ссылки ♻»",
                                           callback_data=menu_callBack.new(button_name="main_menu_links"))

registration_btn = InlineKeyboardButton(text="«Регистрация ✅»",
                                        callback_data=menu_callBack.new(button_name="registration"))

main_menu_keyboard.insert(about_project_btn)
main_menu_keyboard.insert(participate_in_ico_btn)
main_menu_keyboard.insert(commissions_and_taxes_btn)
main_menu_keyboard.insert(presentation_btn)
main_menu_keyboard.insert(partner_program_btn)
main_menu_keyboard.insert(road_map_btn)
main_menu_keyboard.insert(down_w_paper_btn)
main_menu_keyboard.insert(main_menu_links_btn)
main_menu_keyboard.insert(registration_btn)

# список кнопок "Про что вы хотите узнать подробнее"
want_to_know_more_detail = InlineKeyboardMarkup(row_width=1)
safely_safeguard_your_funds_btn = InlineKeyboardButton(text="«Безопасно сберечь ваши средства 🏦»",
                                                       callback_data=menu_callBack.new(
                                                           button_name="safely_safeguard_your_funds"))

increase_rate_growth_btn = InlineKeyboardButton(text="«Гарантированно приумножить рост курса 📈»",
                                                callback_data=menu_callBack.new(button_name="increase_rate_growth"))

earn_on_an_affiliate_program_btn = InlineKeyboardButton(text="«Заработать на партнёрской программе 🤝»",
                                                        callback_data=menu_callBack.new(
                                                            button_name="earn_on_an_affiliate_program"))
want_to_know_more_detail.insert(safely_safeguard_your_funds_btn)
want_to_know_more_detail.insert(increase_rate_growth_btn)
want_to_know_more_detail.insert(earn_on_an_affiliate_program_btn)

# клавиатура приумножить средства
increase_rate_growth_keyboard = InlineKeyboardMarkup(row_width=1)
increase_rate_growth_keyboard.insert(increase_rate_growth_btn)

# клавиатура заработать на партнерской программе
earn_on_an_affiliate_program_keyboard = InlineKeyboardMarkup(row_width=1)
earn_on_an_affiliate_program_keyboard.insert(earn_on_an_affiliate_program_btn)

# список кнопок конца первой части (партнерская программа или вернуться в главное меню)
end_of_first_section_keyboard = InlineKeyboardMarkup(row_width=1)
partner_program = InlineKeyboardButton(text="Партнерская программа🤝",
                                       callback_data=menu_callBack.new(button_name="partner_program_btn"))

back_to_main_menu_from_first = InlineKeyboardButton(text="Вернуться в главное меню ▶",
                                                    callback_data=menu_callBack.new(
                                                        button_name="back_to_main_menu_from_first"))

end_of_first_section_keyboard.insert(partner_program)
end_of_first_section_keyboard.insert(back_to_main_menu_from_first)

# клавиатура "Комиссии, Условия и Тарифы ✍"
commissions_and_taxes_keyboard = InlineKeyboardMarkup(row_width=1)
commissions_and_taxes_keyboard.insert(commissions_and_taxes_btn)

terms_and_commission_keyboard = InlineKeyboardMarkup(row_width=1)
commissions_btn = InlineKeyboardButton(text="Комиссии ✍",
                                       callback_data=menu_callBack.new(button_name="commissions_btn"))

terms_btn = InlineKeyboardButton(text="Условия и Тарифы ✍",
                                 callback_data=menu_callBack.new(button_name="terms_btn"))

terms_and_commission_keyboard.insert(commissions_btn)
terms_and_commission_keyboard.insert(terms_btn)

terms_keyboard = InlineKeyboardMarkup(row_width=1)
terms_keyboard.insert(terms_btn)

tariffs_keyboard = InlineKeyboardMarkup(row_width=1)
tariffs_btn = InlineKeyboardButton(text="Тарифы ✍",
                                   callback_data=menu_callBack.new(button_name="tariffs_btn"))
tariffs_keyboard.insert(tariffs_btn)

# список кнопок конца второй части (Презентация 📣 или вернуться в главное меню)
end_of_second_section_keyboard = InlineKeyboardMarkup(row_width=1)

back_to_main_menu_from_second = InlineKeyboardButton(text="Вернуться в главное меню ▶",
                                                     callback_data=menu_callBack.new(
                                                         button_name="back_to_main_menu_from_first"))

end_of_second_section_keyboard.insert(presentation_btn)
end_of_second_section_keyboard.insert(back_to_main_menu_from_second)

# конец третей части
end_of_third_section_keyboard = InlineKeyboardMarkup(row_width=1)
back_to_main_menu_from_second = InlineKeyboardButton(text="Вернуться в главное меню ▶",
                                                     callback_data=menu_callBack.new(
                                                         button_name="back_to_main_menu_from_first"))
end_of_third_section_keyboard.insert(back_to_main_menu_from_second)
