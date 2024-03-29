from aiogram.fsm.state import State, StatesGroup

class ChoosePaymentCheck(StatesGroup):
    wait_for_idcr = State()
    wait_for_idcb = State()

