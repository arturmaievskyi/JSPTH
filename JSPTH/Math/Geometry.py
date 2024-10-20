import math
from . import MainMath as MM

class GeometryMath():

    def sine(angle_rad: float) -> float:
        return (math.sin(angle_rad))

    def cosine(angle_rad: float) -> float:
        return(math.cos(angle_rad))



    def area_of_circle(radius: float) -> float:
        """
        Calculate the area of a circle.

        Parameters:
        radius (float): The radius of the circle.

        Returns:
        float: The area of the circle.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return(math.pi * radius**2)


    def circumference_of_circle(radius: float) -> float:
        """
        Calculate the circumference of a circle.

        Parameters:
        radius (float): The radius of the circle.

        Returns:
        float: The circumference of the circle.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return(2 * math.pi * radius)


    def volume_of_cone(radius: float, height: float) -> float:
        """
        Calculate the volume of a cone.

        Parameters:
        radius (float): The radius of the cone base.
        height (float): The height of the cone.

        Returns:
        float: The volume of the cone.
        """
        if radius < 0 or height < 0:
            raise ValueError("Radius or height cannot be negative")
        return((1/3) * math.pi * radius**2 * height)

    def surface_area_of_cone(radius: float, slant_height: float) -> float:
        """
        Calculate the surface area of a cone.

        Parameters:
        radius (float): The radius of the cone base.
        slant_height (float): The slant height of the cone.

        Returns:
        float: The surface area of the cone.
        """
        if radius < 0 or slant_height < 0:
            raise ValueError("Radius and slant height cannot be negative")
        return(math.pi * radius * (radius + slant_height))

    def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
        """
        Calculate the distance between two points in 2D space.

        Parameters:
        x1, y1 (float): Coordinates of the first point.
        x2, y2 (float): Coordinates of the second point.

        Returns:
        float: The distance between the two points.
        """
        return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
