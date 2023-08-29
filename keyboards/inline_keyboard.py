from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

question_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
question_menu.button(text="❓ F.A.Q.", callback_data='faq')
question_menu.button(text="📞 Задать вопрос", callback_data='ask_a_question')
question_menu.button(text=" ◀️ Назад ", callback_data='menu')

loyal_card_register_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
# loyal_card_register_menu.button(text=" 💳 Зарегистрировать карту лояльности", callback_data='register')
loyal_card_register_menu.button(text=" 💳 У меня уже есть карта лояльности", callback_data='#')
loyal_card_register_menu.button(text=" ◀️ Назад ", callback_data='menu')

loyal_card_menu_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
loyal_card_menu_keyboard.button(text=" 💳 Мои данные", callback_data='about_user')
loyal_card_menu_keyboard.button(text=" 💳 Баланс карты", callback_data='#')
loyal_card_menu_keyboard.button(text=" ◀️ Назад ", callback_data='menu')

review_dro_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
review_dro_keyboard.button(text="🌐 Яндекс", url='https://yandex.ru/maps/64/kemerovo/chain/mirteck/76675514908/')
review_dro_keyboard.button(text="🌐 2ГИС", url='https://2gis.ru/kemerovo/search/%D0%9C%D0%B8%D1%80%D1%82%D0%B5%D0%BA')
review_dro_keyboard.button(text=" ◀️ Назад", callback_data='menu')

builder_faq: InlineKeyboardBuilder = InlineKeyboardBuilder()
builder_faq.button(text=' 📖 Посмотреть', url='https://mirteck.ru/help/')
builder_faq.button(text=' ◀️ Назад', callback_data='menu')

builder_ask_a_question: InlineKeyboardBuilder = InlineKeyboardBuilder()
builder_ask_a_question.button(text='Задать вопрос менеджеру', url='https://t.me/mirteck_bot')
builder_ask_a_question.button(text=' ◀️ Назад', callback_data='menu')

builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
builder.add(InlineKeyboardButton(text="Подписаться на канал", url='https://t.me/testGroup_v1'))
builder.add(InlineKeyboardButton(text="Зарегистрироваться", callback_data='register'))
builder.add(InlineKeyboardButton(text="Я уже подписан и зарегистрирован", callback_data='done'))

move_to_menu_edit_text: InlineKeyboardBuilder = InlineKeyboardBuilder()
move_to_menu_edit_text.button(text='🔍 МЕНЮ ', callback_data='menu_edit_text')

move_to_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
move_to_menu.button(text='🔍 МЕНЮ ', callback_data='menu')

answer_for_final_question: InlineKeyboardBuilder = InlineKeyboardBuilder()
answer_for_final_question.button(text='Да', callback_data='answer_for_final_question_yes')
answer_for_final_question.button(text='Отмена', callback_data='answer_for_final_question_cancel')
answer_for_final_question.button(text='Пересоздать', callback_data='answer_for_final_question_recreate')
