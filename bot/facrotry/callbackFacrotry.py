from aiogram.filters.callback_data import CallbackData

class CheckInvoice(CallbackData, prefix="Checkinvoice"):
    invoice_id: str
    method: str