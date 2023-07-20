from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

start_keyboard_with_no_auth = InlineKeyboardBuilder()
'''Клавиатура, которая вызывается при комманде /start и условии no_auth'''
start_keyboard_with_no_auth.button(
        text="❓ F.A.Q.",
        callback_data='faq'
)
start_keyboard_with_no_auth.button(
        text="📞 Задать вопрос",
        callback_data='ask_a_question'
)
start_keyboard_with_no_auth.button(
        text="🌐 Перейти на сайт",
        url='https://mirteck.ru/'
)
start_keyboard_with_no_auth.button(
        text="📝 Оставить отзыв",
        callback_data='make_a_review'
)
start_keyboard_with_no_auth.button(
        text="💳 Карта лояльности",
        callback_data='loyal_card_question'
)

start_keyboard_with_auth = InlineKeyboardBuilder()
'''Клавиатура, которая вызывается при комманде /start и условии auth_true'''
start_keyboard_with_auth.button(
        text="❓ F.A.Q.",
        callback_data='faq'
)
start_keyboard_with_auth.button(
        text="📞 Задать вопрос",
        callback_data='ask_a_question'
)
start_keyboard_with_auth.button(
        text="🌐 Перейти на сайт",
        url='https://mirteck.ru/'
)
start_keyboard_with_auth.button(
        text="📝 Оставить отзыв",
        callback_data='make_a_review'
)
start_keyboard_with_auth.button(
        text=" 💳 Мои данные",
        callback_data='about_user'
)
start_keyboard_with_auth.button(
        text=" 💳 Баланс карты",
        callback_data='#'
)

loyal_card_register_menu = InlineKeyboardBuilder()
loyal_card_register_menu.button(
        text=" 💳 Зарегистрировать карту лояльности",
        callback_data='register'
)
loyal_card_register_menu.button(
        text=" 💳 У меня уже есть карта лояльности",
        callback_data='#'
)
loyal_card_register_menu.button(
        text=" ◀️ Назад ",
        callback_data='menu_no_auth'
)
review_dro_keyboard = InlineKeyboardBuilder()
review_dro_keyboard.button(
        text="🌐 Яндекс",
        url='https://yandex.ru/maps/64/kemerovo/chain/mirteck/76675514908/'
)
review_dro_keyboard.button(
        text="🌐 2ГИС",
        url='https://2gis.ru/kemerovo/search/%D0%9C%D0%B8%D1%80%D1%82%D0%B5%D0%BA'
)
review_dro_keyboard.button(
        text=" ◀️ Назад",
        callback_data='menu_no_auth'
)

builder = InlineKeyboardBuilder()
builder.add(InlineKeyboardButton(
        text="Подписаться на канал",
        url='https://t.me/testGroup_v1'))
builder.add(InlineKeyboardButton(
        text="Зарегистрироваться",
        callback_data='register'))
builder.add(InlineKeyboardButton(
        text="Я уже подписан и зарегистрирован",
        callback_data='done'))

builder_faq = InlineKeyboardBuilder()
builder_faq.button(
        text='Часто задаваемые вопросы',
        url='https://mirteck.ru/help/'
)
builder_faq.button(
        text='Вернуться в меню',
        callback_data='menu'
)

builder_move_to_menu = InlineKeyboardBuilder()
builder_move_to_menu.button(
        text='Перейти в меню',
        callback_data='menu'
)

builder_ask_a_question = InlineKeyboardBuilder()
builder_ask_a_question.button(
        text='Задать вопрос менеджеру',
        url='https://t.me/mirteck_bot'
)
builder_ask_a_question.button(
        text='Вернуться в меню',
        callback_data='menu'
)