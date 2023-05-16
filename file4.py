import colorama
from colorama import Fore,Style
print(Fore.RED + "enter token ")
token = input("")
import requests

headers = {
    'Authorization': token
}

def get_user_info():
    response = requests.get('https://discordapp.com/api/users/@me', headers=headers)
    response.raise_for_status()

    user_info = response.json()
    has_phone = 'phone' in user_info and user_info['phone'] is not None
    phone_number = user_info['phone'] if has_phone else 'None'
    email = user_info['email'] if 'email' in user_info else 'None'

    return has_phone, phone_number, email

def has_credit_card():
    response = requests.get('https://discordapp.com/api/users/@me/billing/payment-sources', headers=headers)
    response.raise_for_status()

    payment_sources = response.json()
    return len(payment_sources) > 0

def get_nitro_info():
    response = requests.get('https://discordapp.com/api/users/@me/billing/subscriptions', headers=headers)
    response.raise_for_status()

    subscriptions = response.json()
    has_nitro = len(subscriptions) > 0
    nitro_type = subscriptions[0]['plan']['name'] if has_nitro else 'None'

    return has_nitro, nitro_type

phone, phone_number, email = get_user_info()
has_cc = has_credit_card()
has_nitro, nitro_type = get_nitro_info()

print(f'Phone Number: {phone_number}\nHas Credit Card: {has_cc}\nEmail: {email}\nHas Nitro: {has_nitro}\nNitro Type: {nitro_type}')
input()