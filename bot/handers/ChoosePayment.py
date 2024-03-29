from aiogram import Router
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from bot.state import ChoosePaymentCheck
from bot.facrotry import CheckInvoice
from bot.keyboards import special_agr
from bot.utills import get_status, got_status
import sqlite3

router = Router()


@router.message(StateFilter(ChoosePaymentCheck.wait_for_idcr))
async def choose_amount1(msg: Message, state: FSMContext):
    try:
        invoice_id = msg.text

        await msg.answer(text=f"Агрегатор: CrystalPay\nID: {invoice_id}\nВсё правильно?",
                         reply_markup=special_agr(invoice_id, 'cr'))
        await state.clear()
    except Exception as e:
        await msg.answer(f"Произошла ошибка!\nКод ошибки:{e}")
        await state.clear()


@router.message(StateFilter(ChoosePaymentCheck.wait_for_idcb))
async def choose_amount(msg: Message, state: FSMContext):
    try:
        invoice_id = msg.text
        await msg.answer(text=f"Агрегатор: Cryptobot\nID: {invoice_id}\nВсё правильно?",
                         reply_markup=special_agr(invoice_id, 'cb'))
        await state.clear()
    except Exception as e:
        await msg.answer(f"Произошла ошибка!\nКод ошибки:{e}")
        await state.clear()



@router.callback_query(CheckInvoice.filter())
async def choosen(call: CallbackQuery, callback_data: CheckInvoice):
    invoice_id = callback_data.invoice_id
    method = callback_data.method
    await call.message.edit_text("Проверяю статус счёта.\nВремя ожидание может достигать 30 секунд.")
    if method == 'cb':
        await call.message.edit_text("Проверяю статус счёта..\nВремя ожидание может достигать 30 секунд.")
        if await get_status(invoice_id):
            await call.message.edit_text("Статус счета: Оплачено\n<a href='t.me/vladdrazz'>Создано Vladdra c.</a> ", parse_mode="HTML")
        else:
            await call.message.edit_text("Статус счета: Оплата не найдена\n<a href='t.me/vladdrazz'>Создано Vladdra c.</a> ", parse_mode="HTML")
    elif method == 'cr':
        await call.message.edit_text("Проверяю статус счёта..\nВремя ожидание может достигать 30 секунд.")
        if await got_status(invoice_id):
            await call.message.edit_text("Статус счета: Оплачено\n<a href='t.me/vladdrazz'>Создано Vladdra c.</a> ",parse_mode="HTML")
        else:
            await call.message.edit_text("Статус счета: Оплата не найдена\n<a href='t.me/vladdrazz'>Создано Vladdra c.</a> ", parse_mode="HTML")
    else:
        await call.message.edit_text("Произошла ошибка, попробуйте ещё раз!")


