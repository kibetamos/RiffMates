# mpesa/utils.py

import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
import base64
from datetime import datetime

def get_access_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_url = f"{settings.MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    access_token = response.json().get('access_token')
    return access_token

def lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc):
    access_token = get_access_token()
    api_url = f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()).decode('utf-8')
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://example.com/api/v1/c2b/confirmation",
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
