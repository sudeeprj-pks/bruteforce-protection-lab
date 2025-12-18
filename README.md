# Brute Force Protection Lab (Flask)

## 📘 Project Overview

The **Brute Force Protection Lab** is a Flask-based cybersecurity learning project that demonstrates how **brute-force login attacks work** and how they can be **detected and mitigated** using defensive techniques.

This lab focuses on implementing **basic but effective protections** such as rate limiting, account lockouts, exponential backoff delays, and logging of authentication attempts.

The project is intended for **educational, lab, and SOC learning purposes**.

---

## 🎯 Learning Objectives

* Understand how brute-force attacks target login systems
* Implement defensive controls in a web application
* Learn IP-based throttling and user lockout logic
* Observe attacker behavior through logs and status endpoints

---

## 🔐 Security Controls Implemented

* **IP Rate Limiting** – limits repeated attempts from the same IP
* **User Account Lockout** – locks accounts after multiple failures
* **Exponential Backoff Delay** – increases delay after each failed attempt
* **Login Attempt Logging** – records failed and successful logins
* **Status Endpoint** – visibility into lockouts and IP activity

---

## ✨ Features

* Flask-based login API
* Tracks failed login attempts per IP and user
* Locks users after exceeding failure threshold
* Slows attackers using backoff timing
* `/status` endpoint to monitor security state

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask** (Web Framework)
* Linux / Kali Linux
* curl (for API testing)

---

## 📂 Project Structure

```
bruteforce_lab/
│── defended_server.py   # Main Flask application
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
└── venv/                # Optional Python virtual environment
```

---

## 🚀 Setup & Installation (Kali Linux)

### 1️⃣ Create Project Directory

```bash
mkdir -p ~/lab/bruteforce_lab
cd ~/lab/bruteforce_lab
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

---

## ▶️ Running the Server

```bash
python defended_server.py
```

The server will start on:

* **Login Endpoint:** [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)
* **Status Endpoint:** [http://127.0.0.1:5000/status](http://127.0.0.1:5000/status)

---

## 🧪 Testing the Login API

### ✅ Successful Login

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username":"alice","password":"correcthorsebatterystaple"}' \
http://127.0.0.1:5000/login
```

### ❌ Failed Login

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username":"alice","password":"wrong"}' \
http://127.0.0.1:5000/login
```

Repeated failures will trigger backoff delays and user lockouts.

---

## 📊 Checking System Status

Open in browser or use curl:

```
http://127.0.0.1:5000/status
```

This endpoint displays:

* Failed login attempts per IP
* Locked user accounts
* Current backoff timers

---

## 🔄 How to Restart the Project

If the system is restarted:

```bash
cd ~/lab/bruteforce_lab
source venv/bin/activate
python defended_server.py
```

---

## 🧠 Example Use Cases

* SOC analyst training
* Secure authentication design practice
* Brute-force attack simulation labs
* Flask security learning project

---

## ⚠️ Disclaimer

This project is intended **only for educational and authorized lab environments**. Do not deploy this code in production without additional security hardening.

---

## 📄 License

This project is provided for **learning and academic use**.

---

**Project Title:** Brute Force Protection Lab (Flask)
**Domain:** Web Security • Authentication Defense
**Platform:** Python • Flask
**Author:
