import requests
ip = input("Enter IP address to track: ")

response = requests.get(f"http://ip-api.com/json/{ip}")

if response.status_code == 200:
    data = response.json()
    print(f"IP: {data['query']}")
    print(f"Country: {data['country']}")
    print(f"City: {data['city']}")
    print(f"ISP: {data['isp']}")
else:
    print("Error occurred while tracking IP address")
input()
