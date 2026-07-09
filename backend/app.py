from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    # ВНИМАНИЕ: ВТОРОЙ АРГУМЕНТ - HelloHandler!
    server = HTTPServer(('0.0.0.0', 8080), HelloHandler)
    print("Backend running on port 8080")
    server.serve_forever()