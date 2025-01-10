from elasticsearch import Elasticsearch
import time
import logging

# Initialize Elasticsearch client
es_client = Elasticsearch([{"host": "localhost", "port": 9200}])

class GeolocationLoggingMiddleware:
    """
    Middleware for logging geolocation data to Elasticsearch.
    """

    def __init__(self, index_name="geolocation_logs"):
        self.index_name = index_name

    def log_to_elasticsearch(self, request, geolocation):
        """
        Log geolocation data to Elasticsearch.
        """
        log_entry = {
            "timestamp": int(time.time()),
            "path": request.path,
            "method": request.method,
            "ip_address": request.headers.get("X-Forwarded-For", request.remote_addr),
            "geolocation": geolocation
        }
        try:
            es_client.index(index=self.index_name, document=log_entry)
            logging.info(f"Logged geolocation data to Elasticsearch: {log_entry}")
        except Exception as e:
            logging.error(f"Failed to log geolocation data: {e}")

    def process_request(self, context):
        """
        Process the request to log geolocation data.
        """
        geolocation = context.geolocation
        self.log_to_elasticsearch(context.request, geolocation)
