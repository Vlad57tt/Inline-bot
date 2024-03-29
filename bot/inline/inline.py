from aiogram import Router, F, types

import hashlib
#from bot.keyboards import start_menu, url_button
import os
from dotenv import load_dotenv
from bot.utills import create_invoice, getexchange, creat_invoice, got_status

load_dotenv()
router = Router()

def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


@router.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery):
    try:
        query_parts = inline_query.query.split(maxsplit=2)  # ['method', 'value']
        if len(query_parts) == 2 and query_parts[0].lower() in ['cryptobot','cb', 'crystal', 'cr', 'crystalpay']:
            payment_method = query_parts[0].lower()
            amount = query_parts[1]
            if payment_method in ['cryptobot','cb'] and is_number(amount):
                rates = await getexchange()
                usdt_amount = float(amount) / float(rates)
                total_usdt = usdt_amount * (1 + 15 / 100)
                invoice_link, invoice_id = await create_invoice(price=total_usdt)
                reply_text = f"Метод оплаты: Cryptobot\n💲Сумма:  {amount}₽\n⏰Время на оплату: 15 минут\nID: <code>{invoice_id}</code>\n💸Для оплаты перейдите по ссылке ниже:\n <a href='{invoice_link}'>Перейти к оплате!</a> "
            elif payment_method in ['crystal', 'cr', 'crystalpay'] and is_number(amount):
                total_amount = float(amount) * (1 + 5 / 100)
                invoice_link, invoice_id = await creat_invoice(total_amount)
                if invoice_link and invoice_id != False:
                    reply_text = f"Метод оплаты: CrystalPay\n💲Сумма: {amount}₽\n⏰Время на оплату: 15 минут\nID: <code>{invoice_id}</code>\n💸Для оплаты перейдите по ссылке ниже:\n <a href='{invoice_link}'>Перейти к оплате!</a> "
                else:
                    reply_text = 'Произошла ошибка!'
            input_content = types.InputTextMessageContent(message_text=reply_text, parse_mode="HTML")

            result_id = hashlib.md5(reply_text.encode()).hexdigest()
            item = types.InlineQueryResultArticle(
                id=result_id,
                title='Создать счёт',
                input_message_content=input_content
            )
            await inline_query.answer(results=[item], cache_time=1)
        else:
            # Если запрос пользовательский ввод не соответствует ожидаемому формату,
            # можно отправить сообщение с инструкцией
            instruction_content = types.InputTextMessageContent(
                message_text="Используйте формат: @bot {pay_method} {сумма}, с значениями pay_method вы можете ознакомится в боте в разделе Помощь"
            )
            result_id = hashlib.md5(instruction_content.message_text.encode()).hexdigest()
            instruction_item = types.InlineQueryResultArticle(
                id=result_id,
                title='Инструкция по создание счётов',
                input_message_content=instruction_content
            )
            await inline_query.answer(results=[instruction_item], cache_time=1)
    except Exception as e:
        raise e


