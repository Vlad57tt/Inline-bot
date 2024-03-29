from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.facrotry import CheckInvoice

def start_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="О нас", callback_data="about")
    kb.button(text="Помощь", callback_data="help")
    kb.button(text="Пользовательское соглашение", callback_data="agreement")

    return kb.as_markup()

def back_button() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Назад", callback_data="back")
    return kb.as_markup()

def choose_agregator() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Cryptobot", callback_data="Cryptobot_check")
    kb.button(text="CrystalPay", callback_data="CrystalPay_check")
    return kb.as_markup()

def url_button(url) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Перейти", url=url)
    kb.button(text="Отмена", callback_data="back")

    return kb.as_markup()

def special_agr(id: str, method: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Подтвердить", callback_data=CheckInvoice(invoice_id=id, method=method))
    kb.button(text="Отмена", callback_data="back")
    kb.adjust(2, 1)

    return kb.as_markup()