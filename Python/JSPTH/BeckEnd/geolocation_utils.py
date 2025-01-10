from math import radians, cos, sin, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2) -> float:
    """
    Calculate the great-circle distance between two points on the Earth.

    Args:
        lat1 (float): Latitude of the first location.
        lon1 (float): Longitude of the first location.
        lat2 (float): Latitude of the second location.
        lon2 (float): Longitude of the second location.

    Returns:
        float: Distance in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of Earth in kilometers (mean radius)
    R = 6371.0
    return R * c