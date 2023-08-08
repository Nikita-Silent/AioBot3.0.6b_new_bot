from aiogram.utils.keyboard import InlineKeyboardBuilder


menu_keyboard_with_no_auth: InlineKeyboardBuilder = InlineKeyboardBuilder()
'''Клавиатура, которая вызывается при комманде /start и условии no_auth'''
menu_keyboard_with_no_auth.button(text="❓ Задать вопрос", callback_data='ask')
menu_keyboard_with_no_auth.button(text="🌐 Перейти на сайт", url='https://mirteck.ru/')
menu_keyboard_with_no_auth.button(text="📝 Оставить отзыв", callback_data='make_a_review')
# menu_keyboard_with_no_auth.button(text="💳 Карта лояльности", callback_data='loyal_card_question')
menu_keyboard_with_no_auth.button(text="💳 У меня не работает карта лояльности", callback_data='troubles_with_card')
