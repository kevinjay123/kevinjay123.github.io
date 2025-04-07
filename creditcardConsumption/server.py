from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 允許所有跨域請求
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


PORT = 8000

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
