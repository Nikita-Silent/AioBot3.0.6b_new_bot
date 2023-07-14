from aiogram.fsm.state import StatesGroup, State


class StepsForm (StatesGroup):
    writing_date_of_birth = State()
    writing_mail = State()
    giving_info_about_himself = State()


class StepsFormGroup (StatesGroup):
    shop_chosen = State()
    problem_object_chosen = State()
    reason_written = State()
