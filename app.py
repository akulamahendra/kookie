"""kookie: minimal Python backend with a health endpoint (stdlib only)."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 9000


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok", "service": "kookie"})
        elif self.path == "/":
            self._send(200, {"message": "kookie backend running"})
        else:
            self._send(404, {"error": "not found"})


if __name__ == "__main__":
    print(f"kookie listening on http://0.0.0.0:{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
