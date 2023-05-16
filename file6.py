import requests
import colorama
from colorama import Fore,Style


webhook_url = input(Fore.RED + "Enter the webhook URL: ")

response = requests.delete(webhook_url)

if response.status_code == 204:
    print("Webhook deleted successfully.")
else:
    print("Failed to delete webhook. Status code:", response.status_code)
input()