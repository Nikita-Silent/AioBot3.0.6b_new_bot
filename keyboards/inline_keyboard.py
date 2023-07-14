from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

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

builder_menu_registered = InlineKeyboardBuilder()
builder_menu_registered.button(
        text="FAQ",
        callback_data='faq'
)
builder_menu_registered.button(
        text="Мои данные",
        callback_data='about_user'
)
builder_menu_registered.button(
        text="Перерегистрация",
        callback_data='register'
)
builder_menu_registered.button(
        text="Задать вопрос",
        callback_data='ask_a_question'
)

builder_re_register = InlineKeyboardBuilder()
builder_re_register.button(
        text="Перерегистрация",
        callback_data='register'
)
builder_faq = InlineKeyboardBuilder()
builder_faq.button(
        text='Перейти',
        url='https://mirteck.ru/'
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
        url='https://t.me/Mirteck1'
)
builder_ask_a_question.button(
        text='Вернуться в меню',
        callback_data='menu'
)