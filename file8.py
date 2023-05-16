import os
import tkinter as tk
from tkinter import filedialog
import requests
import colorama
from colorama import Fore,Style
print(Fore.RED + "Locate Your Token List")
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

with open(file_path, 'r') as f:
    for line in f.readlines():
        token = line.strip()
        headers = {
            'Authorization': token
        }
        response = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
        if response.status_code == 200:
            print('\033[92m' + token + '\033[0m')
        else:
            print('\033[91m' + token + '\033[0m')
input()