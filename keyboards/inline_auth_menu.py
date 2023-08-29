from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_keyboard_with_auth: InlineKeyboardBuilder = InlineKeyboardBuilder()
'''Клавиатура, которая вызывается при комманде /start и условии auth_true'''
menu_keyboard_with_auth.button(text="❓ Задать вопрос", callback_data='ask')
menu_keyboard_with_auth.button(text="🌐 Перейти на сайт", url='https://mirteck.ru/')
menu_keyboard_with_auth.button(text="📝 Оставить отзыв", callback_data='make_a_review')
# menu_keyboard_with_auth.button(text="💳 Карта лояльности", callback_data='loyal_card_menu')
menu_keyboard_with_auth.button(text="💳 У меня не работает карта лояльности", callback_data='troubles_with_card')
menu_keyboard_with_auth.button(text="QR (поделиться картой)", callback_data='get_share_qr')
