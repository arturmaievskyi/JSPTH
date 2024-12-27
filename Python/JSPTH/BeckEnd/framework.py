from .http import HttpContext, HttpRequest, HttpResponse
from .securecoockies import SecureCookieManager
from .session import SessionManager

class Framework:
    """Main application framework with integrated session management."""
    def __init__(self, secret_key=None, session_lifetime=3600):
        self.routes = []
        self.middleware = []
        self.session_manager = SessionManager(secret_key=secret_key, session_lifetime=session_lifetime)

    def add_route(self, route):
        self.routes.append(route)

    def add_middleware(self, middleware):
        self.middleware.append(middleware)

    def handle_request(self, http_context):
        # Apply middleware (pre-processing)
        for middleware in self.middleware:
            response = middleware.process_request(http_context)
            if response:
                return response

        # Route resolution
        for route in self.routes:
            if route.matches(http_context.request):
                handler_response = route.handle(http_context)
                if isinstance(handler_response, HttpResponse):
                    return handler_response

        # Return 404 if no route matches
        return HttpResponse(status=404, body="404 Not Found")

    def process_response(self, http_context):
        # Save and finalize session
        http_context.finalize_session()

        # Apply middleware (post-processing)
        for middleware in reversed(self.middleware):
            middleware.process_response(http_context)

    def wsgi_app(self, environ, start_response):
        # Create request, response, and context
        request = HttpRequest(environ)
        response = HttpResponse()
        http_context = HttpContext(request, response, self.session_manager)

        # Handle request
        response = self.handle_request(http_context)

        # Process response
        self.process_response(http_context)

        # Finalize headers and return response
        response.finalize_headers()
        return response(start_response)

    def run(self, host='127.0.0.1', port=8000):
        from wsgiref.simple_server import make_server
        with make_server(host, port, self.wsgi_app) as server:
            print(f"Serving on http://{host}:{port}...")
            server.serve_forever()