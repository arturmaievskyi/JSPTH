import os
import re
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


class HttpRequest:
    def __init__(self, environ):
        self.method = environ["REQUEST_METHOD"]
        self.path = environ["PATH_INFO"]
        self.query_string = environ["QUERY_STRING"]
        self.headers = {key[5:]: value for key, value in environ.items() if key.startswith("HTTP_")}
        self.body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0) or 0)).decode("utf-8")
        self.query_params = parse_qs(self.query_string)
        self.body_params = parse_qs(self.body)


class HttpResponse:
    def __init__(self, body="", status=200, headers=None):
        self.body = body
        self.status = status
        self.headers = headers or [("Content-Type", "text/html")]

    def set_header(self, key, value):
        self.headers.append((key, value))

    def redirect(self, url):
        self.status = 302
        self.set_header("Location", url)


class HttpContext:
    def __init__(self, request: HttpRequest, response: HttpResponse):
        self.request = request
        self.response = response


class Route:
    def __init__(self, path, methods, handler):
        self.path = path
        self.methods = methods
        self.handler = handler
        self.dynamic_match = re.compile(
            re.sub(r"<(\w+)>", r"(?P<\1>[^/]+)", path)
        )  # Convert `/user/<id>` to regex

    def matches(self, path, method):
        return self.dynamic_match.fullmatch(path) and method in self.methods

    def extract_params(self, path):
        match = self.dynamic_match.fullmatch(path)
        return match.groupdict() if match else {}


class Middleware:
    def __init__(self):
        self.pre_request = []
        self.post_request = []

    def add_pre_request(self, func):
        self.pre_request.append(func)

    def add_post_request(self, func):
        self.post_request.append(func)


class WebServer:
    def __init__(self, static_folder="static"):
        self.routes = []
        self.middleware = Middleware()
        self.static_folder = static_folder

    def route(self, path, methods=["GET"]):
        """
        Register a route with the given path and HTTP methods.
        """
        def decorator(func):
            self.routes.append(Route(path, methods, func))
            return func
        return decorator

    def use(self, middleware_func, stage="pre"):
        """
        Add middleware for pre- or post-request stages.
        """
        if stage == "pre":
            self.middleware.add_pre_request(middleware_func)
        elif stage == "post":
            self.middleware.add_post_request(middleware_func)

    def redirect(self, ctx: HttpContext, url):
        """
        Redirect a request to another URL.
        """
        ctx.response.redirect(url)

    def render_template(self, template, **context):
        """
        Render a template using Python string formatting.
        """
        return template.format(**context)

    def send_static_file(self, ctx: HttpContext):
        """
        Serve static files from the static folder.
        """
        static_path = os.path.join(self.static_folder, ctx.request.path.lstrip("/"))
        if os.path.exists(static_path) and os.path.isfile(static_path):
            with open(static_path, "rb") as f:
                content = f.read()
            mime_type = "text/plain"
            if static_path.endswith(".html"):
                mime_type = "text/html"
            elif static_path.endswith(".css"):
                mime_type = "text/css"
            elif static_path.endswith(".js"):
                mime_type = "application/javascript"
            elif static_path.endswith(".png"):
                mime_type = "image/png"
            elif static_path.endswith(".jpg") or static_path.endswith(".jpeg"):
                mime_type = "image/jpeg"
            ctx.response.set_header("Content-Type", mime_type)
            ctx.response.body = content.decode("utf-8")
        else:
            ctx.response.status = 404
            ctx.response.body = "404 Not Found"

    def _make_handler(self, environ, start_response):
        """
        WSGI entry point for handling requests.
        """
        request = HttpRequest(environ)
        response = HttpResponse()
        context = HttpContext(request, response)

        # Apply pre-request middleware
        for middleware in self.middleware.pre_request:
            middleware(context)

        # Route matching
        for route in self.routes:
            if route.matches(request.path, request.method):
                params = route.extract_params(request.path)
                context.request.params = params
                try:
                    route.handler(context)
                except Exception as e:
                    response.status = 500
                    response.body = f"<h1>500 Internal Server Error</h1><pre>{e}</pre>"
                break
        else:
            # Handle static files or 404
            if request.path.startswith(f"/{self.static_folder}"):
                self.send_static_file(context)
            else:
                response.status = 404
                response.body = "<h1>404 Not Found</h1>"

        # Apply post-request middleware
        for middleware in self.middleware.post_request:
            middleware(context)

        status_text = {200: "OK", 302: "Found", 404: "Not Found", 500: "Internal Server Error"}
        status_line = f"{response.status} {status_text.get(response.status, 'Unknown')}"
        start_response(status_line, response.headers)
        return [response.body.encode("utf-8")]

    def run(self, host="127.0.0.1", port=8000):
        """
        Start the WSGI server.
        """
        print(f"Starting server at http://{host}:{port}")
        server = make_server(host, port, self._make_handler)
        server.serve_forever()
