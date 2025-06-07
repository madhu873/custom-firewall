from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json

# Load rules from JSON
with open("rules.json") as f:
    rules = json.load(f)

BLOCKED_KEYWORDS = rules["blocked_keywords"]
BLOCKED_IPS = rules["blocked_ips"]
BACKEND_URL = "http://localhost:3000"

class FirewallHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]

        if self.is_blocked(self.path, client_ip):
            self.log_blocked(client_ip, self.path)
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked by Firewall")
            return

        response = requests.get(BACKEND_URL + self.path)
        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

    def do_POST(self):
        client_ip = self.client_address[0]
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode("utf-8")

        print(f"[POST] From {client_ip}: {post_data}")  # Debug log

        if self.is_blocked(post_data, client_ip):
            self.log_blocked(client_ip, post_data)
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked POST by Firewall")
            return

        response = requests.post(BACKEND_URL + self.path, data=post_data)
        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

    def is_blocked(self, content, ip):
        if ip in BLOCKED_IPS:
            return True
        for keyword in BLOCKED_KEYWORDS:
            if keyword.lower() in content.lower():
                return True
        return False

    def log_blocked(self, ip, content):
        with open("blocked.log", "a") as f:
            f.write(f"Blocked IP: {ip}, Content: {content}\n")

# Start the firewall server
print("🛡️ Firewall running on http://localhost:8080")
httpd = HTTPServer(('0.0.0.0', 8080), FirewallHandler)
httpd.serve_forever()

