
# 🔥 Custom Python Web Application Firewall (WAF)

A lightweight Python-based Web Application Firewall that blocks common XSS and SQL Injection attacks using customizable keyword rules and IP blocking logic.

---

## 📦 Project Structure

```
custom-firewall/
├── firewall.py        # Core WAF logic and reverse proxy
├── backend.py         # Sample Flask backend app
├── rules.json         # Configurable XSS/SQLi/IP block rules
├── blocked.log        # Log file for blocked attempts
```

---

## 🚀 Features

- ✅ Blocks malicious GET and POST requests
- 🔒 Detects XSS, SQLi, UNION attacks, and bad IPs
- 🔁 Acts as a proxy to a backend server (Flask)
- 🧾 Logs blocked IPs and payloads to `blocked.log`
- ⚙️ Easily extendable via `rules.json`

---

## 🛠️ Technologies Used

- Python Standard Library: `http.server`, `requests`, `json`
- Flask (for simulating backend application)
- `curl` (for HTTP request testing)

---

## 📁 Files Overview

### 🔸 `firewall.py`

A Python HTTP proxy server that:

- Intercepts incoming HTTP GET and POST requests
- Checks for blocked keywords (like `<script>`, `SELECT *`, etc.) or IPs
- Logs and blocks malicious traffic
- Forwards clean traffic to a running backend app

### 🔸 `backend.py`

A simple Flask-based web server that:

- Responds to GET requests with a success message
- Echoes POST data received in form submissions

### 🔸 `rules.json`

A JSON file that defines:

- Keywords to block (for detecting XSS/SQLi payloads)
- IP addresses to block

Example:

```json
{
  "blocked_keywords": [
    "<script>",
    "SELECT *",
    "DROP TABLE",
    "alert(",
    "UNION SELECT",
    "' OR '1'='1",
    "1=1",
    "--"
  ],
  "blocked_ips": ["127.0.0.2"]
}
```

### 🔸 `blocked.log`

Log file that records all blocked requests with:

- IP address
- Blocked keyword or path

Example:

```
Blocked IP: 127.0.0.1, Content: <script>alert(1)</script>
```

---

## 🧪 How to Run the Project

### 🔹 Step 1: Install Requirements

```bash
pip install flask requests
```

### 🔹 Step 2: Run the Backend App

```bash
python backend.py
```

This starts the backend on `http://localhost:3000`

### 🔹 Step 3: Start the Firewall

Open a new terminal and run:

```bash
python firewall.py
```

Firewall will run on `http://localhost:8080`

### 🔹 Step 4: Test the Firewall

**XSS Test via Browser:**

```
http://localhost:8080/?q=<script>alert(1)</script>
```

**SQLi Test via curl:**

```bash
curl -X POST http://localhost:8080/ -H "Content-Type: application/x-www-form-urlencoded" -d "username=' OR '1'='1"
```

### 🔹 Step 5: Check the Log

```bash
notepad blocked.log
```

You’ll see entries for all blocked attempts.

---

## 📌 Author

**Madhu** — Cybersecurity & Bug Bounty Researcher

---

## 📜 License

MIT License — Free to use, customize, and enhance.
