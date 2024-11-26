from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import os


class SimpleServer:
    def __init__(self, host='localhost', port=8080, template_dir='templates', static_dir='static'):
        self.host = host
        self.port = port
        self.routes = {}
        self.template_dir = template_dir
        self.static_dir = static_dir

    def route(self, path, methods=['GET']):
        """Decorator to register a function as a route handler for specific paths and methods."""
        def decorator(func):
            for method in methods:
                self.routes[(path, method)] = func
            return func
        return decorator

    def render_template(self, template_name, **context):
        """Render an HTML template, replacing placeholders with context values."""
        template_path = os.path.join(self.template_dir, template_name)
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            for key, value in context.items():
                placeholder = '{{ ' + key + ' }}'
                content = content.replace(placeholder, str(value))
            return content
        except FileNotFoundError:
            print(f"Template '{template_name}' not found.")
            return None

    def send_static_file(self, filename):
        """Serve static files such as CSS, JavaScript, or images."""
        static_path = os.path.join(self.static_dir, filename)
        try:
            with open(static_path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Static file '{filename}' not found.")
            return None

    def run(self):
        """Start the server."""
        server_address = (self.host, self.port)
        httpd = HTTPServer(server_address, self._make_handler())
        print(f"Running on http://{self.host}:{self.port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped.")

    def _make_handler(self):
        """Creates a custom request handler class that can access the SimpleServer instance."""
        server = self
        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self._handle_request('GET')

            def do_POST(self):
                self._handle_request('POST')

            def _handle_request(self, method):
                parsed_path = urlparse(self.path)
                handler = server.routes.get((parsed_path.path, method))
                if handler:
                    handler(self)
                else:
                    static_content = server.send_static_file(parsed_path.path.lstrip('/'))
                    if static_content:
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(static_content)
                    else:
                        self.send_error(404, "File not found")

            def send_html(self, html_content):
                """Helper method to send HTML content."""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_content.encode())
                
        return RequestHandler