from geopy.geocoders import Nominatim
from typing import Optional

class GeolocationMiddleware:
    """
    Middleware for capturing geolocation data from client IPs.
    """

    def __init__(self):
        self.geolocator = Nominatim(user_agent="web_framework_geolocation")

    def get_geolocation(self, ip_address: str) -> Optional[dict]:
        """
        Get geolocation data for an IP address using Geopy.
        
        Args:
            ip_address (str): The client IP address.

        Returns:
            dict: A dictionary containing geolocation data (latitude, longitude, city, country).
        """
        try:
            location = self.geolocator.geocode(ip_address)
            if location:
                return {
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                    "address": location.address
                }
        except Exception as e:
            print(f"Geolocation lookup failed for IP {ip_address}: {e}")
        return None

    def process_request(self, context):
        """
        Process incoming request to attach geolocation metadata.

        Args:
            context (HttpContext): The current HTTP context.
        """
        client_ip = context.request.headers.get("X-Forwarded-For", context.request.remote_addr)
        geolocation = self.get_geolocation(client_ip)
        if geolocation:
            context.geolocation = geolocation
        else:
            context.geolocation = {
                "latitude": None,
                "longitude": None,
                "address": "Unknown"
            }
