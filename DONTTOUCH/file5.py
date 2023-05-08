import random
from termcolor import colored, cprint
import requests

count = int(input("Enter the number of Nitro codes to generate: "))

def nitro_gen(count):
    for i in range(count):
        nitro_code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=16))
        response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true")
        if response.status_code == 200:
            cprint(f"https://discord.gift/{nitro_code}", "green")
        else:
            cprint(f"https://discord.gift/{nitro_code}", "red")

nitro_gen(count)
input()