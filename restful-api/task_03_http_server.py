"""HTTP Handler"""
import http.server
import socketserver
import json


class Site(http.server.BaseHTTPRequestHandler):
    """Basic Site Class"""
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            a = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(a.encode('utf-8'))
        elif self.path == '/info':
            a = json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
                })
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(a.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'Ok')
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def serv_forever(Port):
        with socketserver.TCPServer(("", Port), Site) as httpd:
            print("serving at port", Port)
            httpd.serve_forever()


Site.serv_forever(8000)
