🛡️ Brute Force Protection Lab (Flask)

This project demonstrates how to protect a login system from brute-force attacks using IP throttling, user account locking, backoff delays, and detailed logging.
It is designed for cybersecurity students and developers who want to understand authentication security and defensive programming.

Features
🔒 1. IP-Based Rate Limiting

Tracks failed login attempts per IP

Adds exponential backoff delays

Returns 429 Too Many Requests when throttled

👤 2. User Account Locking

Locks user accounts after too many failed attempts

Tracks failed logins per username

Returns 423 Locked when account is locked
3. Login Attempt Logging

Logs successes, failures, throttled requests

Useful for security monitoring and SIEM labs

📊 4. Internal Status Endpoint

/status returns a live snapshot of IP and user lockout state.
Helpful for testing and observing brute-force mitigation.

Project Structure
bruteforce_lab/
│── app.py                 # Main Flask application
│── requirements.txt        # Dependencies
│── README.md               # Documentation
└── venv/                   # (optional) virtual environment

Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/bruteforce-protection-lab.git
cd bruteforce-protection-lab
(Optional) Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run the Server
python app.py

Your local server starts at:
http://127.0.0.1:5000

PI Endpoints
POST /login

Example request:

{
  "username": "alice",
  "password": "mypassword"
}
Possible responses:

| Status                | Meaning                 |
| --------------------- | ----------------------- |
| 200 OK                | Login successful        |
| 401 Unauthorized      | Wrong username/password |
| 429 Too Many Requests | IP throttled            |
| 423 Locked            | User account locked     |

GET /status

Returns state of:

failed IP attempts

IP backoff timers

user lockout status
Example:
{
  "failed_by_ip_sample": {
    "127.0.0.1": {
      "count": 3,
      "backoff_until": "2025-11-25 12:30:20"
    }
  },
  "failed_by_user_sample": {}
}

Configurable Settings

You can modify these values in app.py:
MAX_FAILED_PER_USER = 5
MAX_FAILED_PER_IP = 50
BACKOFF_BASE_SECONDS = 2     # exponential backoff

Examples:

Lower MAX_FAILED_PER_USER → stronger account lock

Lower MAX_FAILED_PER_IP → stronger IP throttling

Increase BACKOFF_BASE_SECONDS → longer delay each failure


Purpose of This Lab

This project helps you understand:

Defensive design against brute-force attacks

Authentication security mechanisms

How attackers brute-force credentials

Web application rate limiting and lockout policies

Logging patterns useful for SOC & SIEM

Perfect for:

Cybersecurity students

Portfolio projects

Practice labs

Demonstration in interviews


