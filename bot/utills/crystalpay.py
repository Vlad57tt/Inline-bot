
import uuid
import os
import httpx
import random
from dotenv import load_dotenv

load_dotenv()


async def request(data, method: str):
    headers = {'Content-Type': 'application/json'}
    crystal_url = f"https://api.crystalpay.io/v2/{method}/"
    async with httpx.AsyncClient() as client:
        response = await client.post(url=crystal_url, headers=headers, json=data)
    return response.json()



async def creat_invoice(price: float):
    links = [
        'http://vladdra.eu.org/payment_hs82jf8234Lshjf.html',
        'http://vladdra.eu.org/payment_hs238JHs90Jnfj23.html',
        'http://vladdra.eu.org/payment_hs938Kshfdoj98K.html'
    ]
    data = {
        "auth_login": os.getenv("CRYSTAL_LOGIN"),
        "auth_secret": os.getenv("CRYSTAL_SECRET"),
        "amount": price,
        "type": "purchase",
        "description": "ID: " + str(uuid.uuid4()),
        "redirect_url": random.choice(links),
        "lifetime": 900

    }
    r = await request(data=data, method='invoice/create')
    if r["error"]:
        return False, False
    else:
        url, invoice_id = r["url"], r["id"]
        return url, invoice_id

async def got_status(invoice_id: int):
    data = {
        "auth_login": os.getenv("CRYSTAL_LOGIN"),
        "auth_secret": os.getenv("CRYSTAL_SECRET"),
        "id": invoice_id

    }
    r = await request(data=data, method='invoice/info')
    if r["error"]:
        return False
    else:
        status = r["state"]
        if status == "payed":
            return True
        else:
            return False


