"""ACCS121 Sanctuary static host for Cloud Run & Local Dev.
Binds to $PORT (default 8080).
Zero third-party dependencies.
"""
import http.server
import os
import socketserver

PORT = int(os.environ.get("PORT", "8080"))
ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"ACCS121 Sanctuary live at http://localhost:{PORT}")
        httpd.serve_forever()
