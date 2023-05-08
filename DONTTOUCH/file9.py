import requests
import colorama
from colorama import Fore,Style

webhook_url = input(Fore.RED + "Enter the webhook URL: ")
username = input(Fore.RED + "Enter the webhook username: ")
message = input(Fore.RED + "Enter the message to send: ")
count = int(input(Fore.RED + "Enter the number of times to send the message: "))

payload = {
    "content": message,
    "username": username
}

for i in range(count):
    response = requests.post(webhook_url, json=payload)
    print(Fore.RED + f"{i+1} SPAM STILL UP")
