from aiogram import Router, F
from bot.keyboards import choose_agregator
from aiogram.types import Message
from dotenv import load_dotenv
import os

router = Router()
load_dotenv()



def check_user_id(user_id):
    accepted_users = os.getenv('ACCEPTED_USER')
    accepted_user_ids = [int(user_id) for user_id in accepted_users.split(',')]
    return user_id in accepted_user_ids
def check_user(user_id):
    if check_user_id(user_id):
        return True
    else:
        return False

@router.message(F.text == "/check")
async def start(msg: Message):
    user_id = msg.from_user.id
    if check_user(user_id):
        await msg.answer("Выберите платёжного агрегатора", reply_markup=choose_agregator())
    else:
        await msg.answer(f"Данная функция недоступна для вашего статуса!\nВаш ID:<code>{user_id}</code>", parse_mode="HTML")


