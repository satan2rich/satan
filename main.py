import os
import subprocess
from colorama import Fore, Style
import subprocess
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


folder_path = os.getcwd()

file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


file_map = {}
for i, file_name in enumerate(file_names):
    file_number = str(i + 1)
    file_map[file_number] = os.path.join(folder_path, file_name)

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

command = input(Fore.RED)

if command == "1":
    subprocess.run(['python', 'file1.py'])
elif command == "2":
    subprocess.run(['python', 'file2.py'])
elif command == "3":
    subprocess.run(['python', 'file3.py'])
elif command == "4":
    subprocess.run(['python', 'file4.py'])
elif command == "5":
    subprocess.run(['python', 'file5.py'])
elif command == "8":
    subprocess.run(['python', 'file8.py'])
elif command == "9":
    subprocess.run(['python', 'file9.py'])
elif command == "7":
    subprocess.run(['python', 'file7.py'])
elif command == "6":
    subprocess.run(['python', 'file6.py'])
elif command == "10":
    subprocess.run(['python', 'file10.py'])
