import os
import subprocess
from colorama import Fore, Style
text = (Fore.RED + "                                   ██████  ▄▄▄     ▄▄▄█████▓ ▄▄▄       ███▄    █\n"
        "                                   ▒██    ▒ ▒████▄   ▓  ██▒ ▓▒▒████▄     ██ ▀█   █\n"
        "                                   ░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒\n"
        "                                     ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n"
        "                                   ▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░\n"
        "                                   ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n"
        "                                   ░ ░▒  ░ ░  ▒   ▒▒ ░   ░      ▒   ▒▒ ░░ ░░   ░ ▒░\n"
        "                                   ░  ░  ░    ░   ▒    ░        ░   ▒      ░   ░ ░ \n"
        "                                         ░        ░  ░              ░  ░         ░ " + Style.RESET_ALL)
print(text)
print(Fore.RED + "                                        If You Bought This You Got Scammed")
print(Fore.RED + "                                       ======================================" + Style.RESET_ALL)
print(Fore.RED + "                                        https://github.com/satan2rich/satan")
print(Fore.RED + "                                         ")
print(Fore.RED + "                                         " + Style.RESET_ALL)
from colorama import Fore, Style

# set the folder name
folder_name = "DONTTOUCH"

# get the path to the folder
folder_path = os.path.join(os.getcwd(), folder_name)

# check if the folder exists
if not os.path.exists(folder_path):
    print(Fore.RED + f"Folder '{folder_name}' does not exist!" + Style.RESET_ALL)
    exit()

# get the file names in the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# map the file names to their corresponding numbers
file_map = {}
for i, file_name in enumerate(file_names):
    file_number = str(i + 1)
    file_map[file_number] = os.path.join(folder_path, file_name)

# print the menu
print("[" + Fore.RED + "1" + Style.RESET_ALL + "] " + Fore.RED + "DDOS          " + Style.RESET_ALL +
      "       [" + Fore.RED + "2" + Style.RESET_ALL + "] " + Fore.RED + "IpLookup" + Style.RESET_ALL +
      "       [" + Fore.RED + "3" + Style.RESET_ALL + "] " + Fore.RED + "CC GEN  " + Style.RESET_ALL +
      "       [" + Fore.RED + "4" + Style.RESET_ALL + "] " + Fore.RED + "TokenLookUp    " + Style.RESET_ALL +
      "       [" + Fore.RED + "5" + Style.RESET_ALL + "] " + Fore.RED + "NitroGen" + Style.RESET_ALL)
print("[" + Fore.RED + "6" + Style.RESET_ALL + "] " + Fore.RED + "Webhook Delete" + Style.RESET_ALL +
      "       [" + Fore.RED + "7" + Style.RESET_ALL + "] " + Fore.RED + "Credits" + Style.RESET_ALL +
      "        [" + Fore.RED + "8" + Style.RESET_ALL + "] " + Fore.RED + "Token Checker" + Style.RESET_ALL +
      "  [" + Fore.RED + "9" + Style.RESET_ALL + "] " + Fore.RED + "Webhook Spammer" + Style.RESET_ALL +
      "       [" + Fore.RED + "10" + Style.RESET_ALL + "] " + Fore.RED + "Roblox Giftcard Gen" + Style.RESET_ALL)
# get the user's choice and execute the corresponding file
command = input(Fore.RED)
if command in file_map:
    subprocess.run(['python', file_map[command]])
else:
    print(Fore.RED + "Invalid command!" + Style.RESET_ALL)
