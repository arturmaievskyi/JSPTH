# middleware.py

from typing import Callable
from redis_session import RedisSessionStore
from http import HTTPStatus


class SessionAuthenticationMiddleware:
    """
    Middleware to authenticate users based on Redis-backed session data.
    """

    def __init__(self, app: Callable, redis_session_store: RedisSessionStore):
        """
        Initialize the middleware.

        Args:
            app (Callable): The downstream application.
            redis_session_store (RedisSessionStore): The Redis session manager.
        """
        self.app = app
        self.redis_session_store = redis_session_store

    def __call__(self, environ: dict, start_response: Callable):
        """
        Handle incoming requests and validate sessions.

        Args:
            environ (dict): The WSGI environment dictionary.
            start_response (Callable): The WSGI start response callable.

        Returns:
            Callable: The response from the downstream application.
        """
        # Extract the session ID from cookies
        cookies = self._parse_cookies(environ)
        session_id = cookies.get("session_id")

        if not session_id:
            # No session ID, return 401 Unauthorized
            return self._unauthorized_response(start_response)

        # Retrieve session data
        session_data = self.redis_session_store.get_session(session_id)

        if not session_data:
            # Invalid or expired session, return 401 Unauthorized
            return self._unauthorized_response(start_response)

        # Add session data to the environment for downstream use
        environ["session_data"] = session_data

        # Call the downstream application
        return self.app(environ, start_response)

    def _parse_cookies(self, environ: dict) -> dict:
        """
        Parse the cookies from the HTTP headers.

        Args:
            environ (dict): The WSGI environment dictionary.

        Returns:
            dict: A dictionary of cookies.
        """
        cookies = {}
        if "HTTP_COOKIE" in environ:
            cookie_header = environ["HTTP_COOKIE"]
            for cookie in cookie_header.split(";"):
                name, value = cookie.strip().split("=", 1)
                cookies[name] = value
        return cookies

    def _unauthorized_response(self, start_response: Callable):
        """
        Return a 401 Unauthorized response.

        Args:
            start_response (Callable): The WSGI start response callable.

        Returns:
            List[bytes]: The HTTP response body.
        """
        start_response(
            f"{HTTPStatus.UNAUTHORIZED.value} {HTTPStatus.UNAUTHORIZED.phrase}",
            [("Content-Type", "text/plain")],
        )
        return [b"401 Unauthorized - Invalid or missing session."]
