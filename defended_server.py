# defended_server.py
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import logging

app = Flask(__name__)

# ===== In-memory user DB (lab only) =====
USERS = {
    "alice": "correcthorsebatterystaple",
    "bob": "S3cureP@ss"
}

failed_by_ip = {}       # ip -> {count, last_failed_at, backoff_until}
failed_by_user = {}     # username -> {count, locked_until}

# thresholds
MAX_FAILED_PER_USER = 5
MAX_FAILED_PER_IP = 50
BACKOFF_BASE_SECONDS = 2  # exponential backoff base

logging.basicConfig(filename='login_attempts.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def record_failure(ip, username):
    now = datetime.utcnow()
    ip_state = failed_by_ip.setdefault(ip, {"count": 0, "last_failed_at": None, "backoff_until": None})
    ip_state["count"] += 1
    ip_state["last_failed_at"] = now
    backoff_seconds = BACKOFF_BASE_SECONDS ** min(ip_state["count"], 6)
    ip_state["backoff_until"] = now + timedelta(seconds=backoff_seconds)

    user_state = failed_by_user.setdefault(username, {"count": 0, "locked_until": None})
    user_state["count"] += 1
    if user_state["count"] >= MAX_FAILED_PER_USER:
        user_state["locked_until"] = now + timedelta(minutes=15)

def is_ip_throttled(ip):
    state = failed_by_ip.get(ip)
    if not state:
        return False
    if state.get("backoff_until") and state["backoff_until"] > datetime.utcnow():
        return True
    if state["count"] > MAX_FAILED_PER_IP:
        return True
    return False

def is_user_locked(username):
    state = failed_by_user.get(username)
    if not state:
        return False
    locked_until = state.get("locked_until")
    if locked_until and locked_until > datetime.utcnow():
        return True
    return False

# ========== LOGIN POST ENDPOINT ==========
@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr or "unknown"
    data = request.get_json(force=True)
    username = data.get("username", "")
    password = data.get("password", "")

    if is_ip_throttled(ip):
        logging.warning(f"IP throttled: {ip} username={username}")
        return jsonify({"success": False, "error": "Too many requests from this IP. Try later."}), 429

    if is_user_locked(username):
        logging.warning(f"User locked: {username} from IP {ip}")
        return jsonify({"success": False, "error": "Account locked. Try again later."}), 423

    expected = USERS.get(username)
    if expected and password == expected:
        failed_by_user.pop(username, None)
        logging.info(f"Successful login: {username} from {ip}")
        return jsonify({"success": True, "message": "Logged in"}), 200
    else:
        record_failure(ip, username)
        logging.info(f"Failed login attempt: username={username} ip={ip}")
        return jsonify({"success": False, "error": "Invalid credentials"}), 401

# ========== NEW LOGIN GET ENDPOINT ==========
@app.route("/login", methods=["GET"])
def login_get():
    return jsonify({
        "message": "Use POST request for login. Browser GET is not supported."
    }), 200

# ========== STATUS ENDPOINT ==========
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "failed_by_ip_sample": {
            k: {"count": v["count"], "backoff_until": str(v["backoff_until"])}
            for k, v in list(failed_by_ip.items())[:10]
        },
        "failed_by_user_sample": {k: v for k, v in list(failed_by_user.items())[:10]}
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

