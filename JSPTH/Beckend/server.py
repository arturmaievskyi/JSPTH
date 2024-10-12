from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


def run_serve(port = 1234):
    server_adress = ('', port)
    httpd = HTTPServer(server_adress, BaseHTTPRequestHandler)
    print(f"http.localhost:{port}")