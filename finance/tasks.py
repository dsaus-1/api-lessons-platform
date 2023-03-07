from config import settings
from finance.models import Payment
import requests
import hashlib


def check_status_payment():
    payment = Payment.objects.filter(payment_method=Payment.METHOD_TRANSFER, status=Payment.CREATED)

    for pay in payment:
        hash_token = hashlib.sha256(f"{settings.TERMINAL_PASSWORD}{pay.payment_id_tinkoff}{settings.TERMINAL_KEY}".encode())
        token = hash_token.hexdigest()

        data = {
            "TerminalKey": settings.TERMINAL_KEY,
            "PaymentId": pay.payment_id_tinkoff,
            "Token": token
        }

        request = requests.post('https://securepay.tinkoff.ru/v2/GetState', json=data)

        if request.json().get('Status') == 'REJECTED':
            pay.status = Payment.REJECTED
            pay.save()
        elif request.json().get('Status') == 'CONFIRMED':
            pay.status = Payment.CONFIRMED
            pay.save()