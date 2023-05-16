import random
import string
import requests
import re
from colorama import Fore,Style
print(Fore.RED + "how many giftcards would you like to generate")
count = input()
url = 'https://www.roblox.com/gamecards/redeem'
pattern = re.compile(r'<h3>(.+?)</h3>')

def generate_giftcard():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(18))

def check_giftcard(giftcard):
    response = requests.post(url, data={'giftcard': giftcard})
    if "Invalid Code" in response.text:
        print(Fore.GREEN + f"Giftcard redeemed successfully: {giftcard}")
        return True
    else:
        print(Fore.RED + f"Invalid Giftcard: {giftcard}")
        return False


for i in range(int(count)):
    giftcard = generate_giftcard()
    check_giftcard(giftcard)
