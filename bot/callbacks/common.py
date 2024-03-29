from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards import start_menu, url_button, back_button
import os
from dotenv import load_dotenv

load_dotenv()
router = Router()


@router.callback_query(F.data == "back")
async def donate(call: CallbackQuery):
    await call.message.edit_text("Добро пожаловать в нашего инлайн бота!", reply_markup=start_menu())


@router.callback_query(F.data == "about")
async def about(call: CallbackQuery):
    await call.message.edit_text("Чтобы узнать о нас побольше просто перейдите по кнопке ниже!", reply_markup=url_button(os.getenv("URL_ABOUT")))

@router.callback_query(F.data == "help")
async def help(call: CallbackQuery):
    await call.message.edit_text("""
Привет, друг! 🙌 Готов создать счёт мгновенно? "СчетоМастерБот" (@bot) пришёл на помощь! 🚀

*Как создавать счёта?* 🛠️
Просто введи в любом чате:
`@bot cryptobot 1` (или `cb`), где 1 это ваша сумма! Для платежей через Cryptobot.
Или:
`@bot crystal 1` (или `cr` или `crystalpay`), где 1 это ваша сумма! Для платежей через CrystalPay.

Счёт готовится к отправке моментально! ✨

*Хочешь узнать статус счёта?* 🔍
Следуй этим шагам:
1️⃣ Отправь команду `/check` в личных сообщениях бота.
2️⃣ Выбери платёжный агрегатор: Cryptobot или CrystalPay.
3️⃣ Введи уникальный ID счёта.
4️⃣ Нажми "Подтвердить" и всего через 5 секунд получи все данные по твоему счёту! ⏱️

Если возникнут вопросы, обращайся - "СчетоМастерБот" всегда к твоим услугам! 😉

Создавай, проверяй и наслаждайся процессом!
Твой "СчетоМастерБот" 🤖💙
P.S: Комманда `/check` не доступна для пользователей не оплативших подписку; Средства поступают на счёт бота,
вы вправе запросить выплату, но не забудьте указать уникальный идентификатор платежа при обращение к команде.

    """, reply_markup=back_button())


@router.callback_query(F.data == "agreement")
async def agreement(call: CallbackQuery):
    await call.message.edit_text("Чтобы прочитать пользовательское соглашение просто перейдите по кнопке ниже!", reply_markup=url_button(os.getenv("URL_AGREEMENT")))


