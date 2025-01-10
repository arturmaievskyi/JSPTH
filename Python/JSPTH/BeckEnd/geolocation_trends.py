import requests
import json
from datetime import datetime

# Elasticsearch Config
ES_URL = "http://localhost:9200"
INDEX_NAME = "geolocation_logs"

def query_top_locations():
    """
    Query Elasticsearch for the top locations by request count.
    """
    query = {
        "size": 0,
        "aggs": {
            "top_locations": {
                "terms": {
                    "field": "geolocation.address.keyword",
                    "size": 10
                },
                "aggs": {
                    "request_count": {
                        "value_count": {
                            "field": "_id"
                        }
                    }
                }
            }
        }
    }
    response = requests.post(f"{ES_URL}/{INDEX_NAME}/_search", json=query)
    data = response.json()
    print("Top Locations by Request Count:")
    for bucket in data["aggregations"]["top_locations"]["buckets"]:
        print(f"{bucket['key']}: {bucket['doc_count']} requests")


def query_trends_by_region(top_left, bottom_right, start_date, end_date):
    """
    Query Elasticsearch for request trends over time in a specific region.
    
    Args:
        top_left (dict): Coordinates of the top-left corner of the bounding box.
        bottom_right (dict): Coordinates of the bottom-right corner of the bounding box.
        start_date (str): Start date in ISO format (e.g., "2023-01-01").
        end_date (str): End date in ISO format (e.g., "2023-12-31").
    """
    query = {
        "query": {
            "bool": {
                "filter": [
                    {
                        "geo_bounding_box": {
                            "geolocation": {
                                "top_left": top_left,
                                "bottom_right": bottom_right
                            }
                        }
                    },
                    {
                        "range": {
                            "timestamp": {
                                "gte": start_date,
                                "lte": end_date
                            }
                        }
                    }
                ]
            }
        },
        "aggs": {
            "request_trends": {
                "date_histogram": {
                    "field": "timestamp",
                    "calendar_interval": "day"
                }
            }
        },
        "size": 0
    }
    response = requests.post(f"{ES_URL}/{INDEX_NAME}/_search", json=query)
    data = response.json()
    print(f"Request Trends from {start_date} to {end_date} for Region:")
    for bucket in data["aggregations"]["request_trends"]["buckets"]:
        date = datetime.utcfromtimestamp(bucket["key"] / 1000).strftime("%Y-%m-%d")
        print(f"{date}: {bucket['doc_count']} requests")

