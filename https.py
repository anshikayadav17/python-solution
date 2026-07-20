from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8080


class MyServer(BaseHTTPRequestHandler):

    def send_html(self, html, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())

    def do_GET(self):

        if self.path == "/":
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Python HTTP Server</title>
            </head>
            <body>
                <h1>Welcome to Python HTTP Server</h1>
                <p>Current Time:</p>
                <h2>{datetime.now()}</h2>

                <hr>

                <a href="/">Home</a><br>
                <a href="/about">About</a><br>
                <a href="/contact">Contact</a><br>
            </body>
            </html>
            """
            self.send_html(html)

        elif self.path == "/about":
            html = """
            <html>
            <body>
                <h1>About Page</h1>
                <p>This server is written completely in Python.</p>
                <a href="/">Back</a>
            </body>
            </html>
            """
            self.send_html(html)

        elif self.path == "/contact":
            html = """
            <html>
            <body>
                <h1>Contact Page</h1>
                <p>Email: admin@example.com</p>
                <a href="/">Back</a>
            </body>
            </html>
            """
            self.send_html(html)

        else:
            html = """
            <html>
            <body>
                <h1>404 - Page Not Found</h1>
                <a href="/">Home</a>
            </body>
            </html>
            """
            self.send_html(html, 404)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyServer)

    print("=" * 50)
    print("Python HTTP Server")
    print(f"Running on http://{HOST}:{PORT}")
    print("=" * 50)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
