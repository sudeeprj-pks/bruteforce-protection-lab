Brute Force Protection Lab (Flask)

This project is a hands-on cybersecurity lab demonstrating how to protect a login endpoint from brute-force attacks using:

IP-Based Throttling

User Account Locking

Backoff Timers

Logging of failed & successful attempts

Status endpoint to observe throttling behavior

It is designed for cybersecurity students, SOC analysts, and developers who want to understand web authentication hardening.

 Features
 1. IP-Based Rate Limiting

Blocks repeated login attempts from the same IP after multiple failures.

Tracks failed attempts per IP

Applies backoff delays

Returns HTTP 429 Too Many Requests

 2. User Account Locking

Locks a user account for a specific time after several failed attempts.

Tracks failed attempts per username

Locks account temporarily

Returns HTTP 423 Locked

 3. Logging

Logs:

Successful logins

Failed logins

Throttled IPs

Locked accounts

Useful for cybersecurity monitoring.

4. Status Endpoint

/status

Shows:

    failed_by_ip_sample

    failed_by_user_sample

Useful for testing and debugging.
Project Structure

bruteforce_lab/
│── app.py                 # Flask API with brute-force protection
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
└── venv/                   # (optional) Python virtual environment

 Installation & Setup
1️ Clone the repository

git clone https://github.com/<your-username>/bruteforce-protection-lab.git
cd bruteforce-protection-lab

2️ Create Virtual Environment (optional)

python3 -m venv venv
source venv/bin/activate

3️ Install Dependencies

pip install -r requirements.txt

4️ Run the Server

python app.py

Server starts at:

http://127.0.0.1:5000

API Endpoints
POST /login

Login request:

{
  "username": "admin",
  "password": "password123"
}

Responses:

    200 OK → Login successful

    401 Unauthorized → Wrong credentials

    429 Too Many Requests → IP throttled

    423 Locked → Account locked

GET /status

Shows throttling and lockout information:

{
  "failed_by_ip_sample": {
    "127.0.0.1": {
      "count": 2,
      "backoff_until": "2025-11-25 16:32:20"
    }
  },
  "failed_by_user_sample": {}
}

Configuration

Inside app.py, you can tune parameters:

MAX_IP_FAILURES = 5
IP_BACKOFF_SECONDS = 30

MAX_USER_FAILURES = 3
USER_LOCK_SECONDS = 60

Change these values to adjust the security strength.
 Purpose of the Project

This project helps you understand and implement brute-force mitigation, similar to:

    Web application firewalls

    SIEM brute-force alerts

    Authentication hardening practices

    OWASP rate-limiting guidelines
Access internal state:
