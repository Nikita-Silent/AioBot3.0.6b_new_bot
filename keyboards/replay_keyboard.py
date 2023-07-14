from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
        Создаёт реплай-клавиатуру с кнопками в один ряд
        :param items: список текстов для кнопок
        :return: объект реплай-клавиатуры
        """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True, one_time_keyboard=True, selective=True)


contact_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Поделиться контактом',
            request_contact=True
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, selective=True
)
