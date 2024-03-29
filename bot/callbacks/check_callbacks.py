from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards import back_button
from aiogram.fsm.context import FSMContext
from bot.state import ChoosePaymentCheck

router = Router()


@router.callback_query(F.data == "CrystalPay_check")
async def donate(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите уникальный идентификатор платежа:", reply_markup=back_button())
    await state.set_state(ChoosePaymentCheck.wait_for_idcr)



@router.callback_query(F.data == "Cryptobot_check")
async def donate(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.edit_text("Введите уникальный идентификатор платежа:", reply_markup=back_button())
        await state.set_state(ChoosePaymentCheck.wait_for_idcb)
    except Exception as e:
        await call.message.edit_text(f"Произошла ошибка!\nКод ошибки:{e}")

