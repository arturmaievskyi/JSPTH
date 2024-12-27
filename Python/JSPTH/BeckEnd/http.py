from http.cookies import SimpleCookie
from urllib.parse import parse_qs, urlencode
import json
from .securecoockies import SecureCookieManager

class HttpRequest:
    """Represents an HTTP request."""
    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD', 'GET')
        self.path = environ.get('PATH_INFO', '/')
        self.query_string = environ.get('QUERY_STRING', '')
        self.headers = self._parse_headers(environ)
        self.body = self._read_body(environ)
        self.cookies = self._parse_cookies()
        self.params = parse_qs(self.query_string)

    def _parse_headers(self, environ):
        """Parse HTTP headers from the WSGI environment."""
        return {
            k[5:].replace('_', '-').title(): v
            for k, v in environ.items()
            if k.startswith('HTTP_')
        }

    def _read_body(self, environ):
        """Read the request body."""
        try:
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            return environ['wsgi.input'].read(content_length).decode('utf-8') if content_length else ''
        except (ValueError, KeyError):
            return ''

    def _parse_cookies(self):
        """Parse cookies from the 'Cookie' header."""
        cookie_header = self.headers.get('Cookie', '')
        return SimpleCookie(cookie_header)

    def json(self):
        """Parse JSON body."""
        try:
            return json.loads(self.body)
        except json.JSONDecodeError:
            return {}


class HttpResponse:
    """Represents an HTTP response with secure cookie management."""
    def __init__(self, body='', status=200, headers=None, secret_key=None):
        self.body = body
        self.status = status
        self.headers = headers or [('Content-Type', 'text/plain')]
        self.cookies = SimpleCookie()
        self.secure_cookie_manager = SecureCookieManager(secret_key)

    def set_cookie(self, key, value, encrypt=False, max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None):
        """
        Set a cookie with optional encryption and advanced options.

        Args:
            key (str): Cookie name.
            value (str or dict): Cookie value.
            encrypt (bool): Whether to encrypt the cookie value.
            max_age (int, optional): Lifetime of the cookie in seconds.
            expires (str, optional): Expiration date in GMT format.
            path (str, optional): URL path for which the cookie is valid (default is '/').
            domain (str, optional): Domain for which the cookie is valid.
            secure (bool, optional): Whether the cookie is sent only over HTTPS.
            httponly (bool, optional): Whether the cookie is accessible only via HTTP (not JavaScript).
            samesite (str, optional): SameSite policy ('Strict', 'Lax', or 'None').
        """
        if encrypt:
            value = self.secure_cookie_manager.encrypt(value)
        self.cookies[key] = value

        # Set standard attributes
        if max_age is not None:
            self.cookies[key]['max-age'] = str(max_age)
        if expires is not None:
            self.cookies[key]['expires'] = expires
        self.cookies[key]['path'] = path
        if domain is not None:
            self.cookies[key]['domain'] = domain
        if secure:
            self.cookies[key]['secure'] = True
        if httponly:
            self.cookies[key]['httponly'] = True

        # Set SameSite policy
        if samesite is not None:
            if samesite.lower() not in ['strict', 'lax', 'none']:
                raise ValueError("Invalid value for SameSite: must be 'Strict', 'Lax', or 'None'.")
            self.cookies[key]['samesite'] = samesite.capitalize()

    def get_cookie(self, key, decrypt=False):
        """Retrieve a cookie value, optionally decrypting it."""
        if key not in self.cookies:
            return None
        value = self.cookies[key].value
        if decrypt:
            return self.secure_cookie_manager.decrypt(value)
        return value

    def delete_cookie(self, key, path='/', domain=None):
        """
        Delete a cookie by setting its expiry in the past.

        Args:
            key (str): Cookie name.
            path (str, optional): URL path for which the cookie is valid (default is '/').
            domain (str, optional): Domain for which the cookie is valid.
        """
        self.set_cookie(key, '', max_age=0, path=path, domain=domain)

    def finalize_headers(self):
        """Prepare headers for the WSGI response."""
        for morsel in self.cookies.values():
            self.headers.append(('Set-Cookie', morsel.OutputString()))

    def __call__(self, start_response):
        """Prepare the response for the WSGI server."""
        status_line = f'{self.status} {self._get_status_message()}'
        self.finalize_headers()
        start_response(status_line, self.headers)
        return [self.body.encode('utf-8')]

    def _get_status_message(self):
        """Get the message for the HTTP status code."""
        messages = {
            200: 'OK',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found',
            500: 'Internal Server Error',
        }
        return messages.get(self.status, 'Unknown Status')

class HttpContext:
    """Encapsulates an HTTP request and response."""
    def __init__(self, request, response, session_manager):
        self.request = request
        self.response = response
        self.session_manager = session_manager
        self.session_id = None
        self.session = None

        # Load session
        encrypted_session_id = request.cookies.get(session_manager.cookie_name, None)
        if encrypted_session_id:
            self.session_id, self.session = session_manager.get_session(encrypted_session_id)
        
        # Create a new session if none exists
        if not self.session:
            self.session_id, self.session = session_manager.create_session()
    
    def finalize_session(self):
        """Encrypt and save the session ID in the response."""
        encrypted_session_id = self.session_manager.cookie_manager.encrypt(self.session_id, max_age=self.session_manager.session_lifetime)
        self.response.set_cookie(
            key=self.session_manager.cookie_name,
            value=encrypted_session_id,
            max_age=self.session_manager.session_lifetime,
            secure=True,
            httponly=True,
            samesite="Strict"
        )
        self.session_manager.save_session(self.session_id, self.session)