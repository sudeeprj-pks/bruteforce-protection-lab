Brute Force Protection Lab (Flask)

This project is a simple Flask-based login system that includes basic brute-force protection, such as:

IP rate limiting

User account lockout

Exponential backoff delay

Logging failed and successful attempts

It is designed as a cybersecurity learning project to understand how brute-force attacks work and how to defend against them.

📌 Features

✔️ Login endpoint using Flask

✔️ Tracks failed login attempts

✔️ Locks users after too many failed attempts

✔️ Slows down attackers with backoff delay

✔️ Shows the current lockout status using /status

📁 Project Files
bruteforce_lab/
│── defended_server.py   # Main Flask application
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
└── venv/                # Optional Python virtual environment

🛠️ Steps You Followed in This Project (Simple Explanation)

This is what you have done in your Kali Linux machine:
1️⃣ Created project folder

mkdir -p ~/lab/bruteforce_lab
cd ~/lab/bruteforce_lab

2️⃣ Created Python virtual environment

python3 -m venv venv
source venv/bin/activate

3️⃣ Installed Flask

pip install flask

4️⃣ Created defended_server.py

This file contains:

    Login API

    Brute-force protection logic

    User lockout rules

    IP throttling rules

5️⃣ Ran the server

python defended_server.py

Server runs on:

👉 http://127.0.0.1:5000/login

👉 http://127.0.0.1:5000/status
6️⃣ Tested login using curl

Successful login:

curl -X POST -H "Content-Type: application/json" \
-d '{"username":"alice","password":"correcthorsebatterystaple"}' \
http://127.0.0.1:5000/login

Failed login:

curl -X POST -H "Content-Type: application/json" \
-d '{"username":"alice","password":"wrong"}' \
http://127.0.0.1:5000/login

7️⃣ Checked status

http://127.0.0.1:5000/status

Shows lockouts and IP failures.
▶️ How to Run the Project Again

If you restart or reopen the PC:

cd ~/lab/bruteforce_lab
source venv/bin/activate
python defended_server.py
API Endpoints
POST /login

Used to check login.

GET /status

Shows:

Failed attempts per IP

User lockouts

Backoff timers

