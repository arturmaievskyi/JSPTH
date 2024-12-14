class GeometryUtils {
    constructor() {}
  
    // Area of a Circle: π * r²
    area_of_circle(radius) {
      if (radius < 0) throw new Error("Radius cannot be negative.");
      return Math.PI * radius ** 2;
    }
  
    // Circumference of a Circle: 2 * π * r
    circumference_of_circle(radius) {
      if (radius < 0) throw new Error("Radius cannot be negative.");
      return 2 * Math.PI * radius;
    }
  
    // Volume of a Cone: (1/3) * π * r² * h
    volume_of_cone(radius, height) {
      if (radius < 0 || height < 0) throw new Error("Radius and height cannot be negative.");
      return (1 / 3) * Math.PI * radius ** 2 * height;
    }
  
    // Surface Area of a Cone: π * r * (r + l), where l = slant height
    surface_area_of_cone(radius, height) {
      if (radius < 0 || height < 0) throw new Error("Radius and height cannot be negative.");
      const slantHeight = Math.sqrt(radius ** 2 + height ** 2);
      return Math.PI * radius * (radius + slantHeight);
    }
  
    // Distance Between Two Points: √((x2 - x1)² + (y2 - y1)²)
    distance_between_points(x1, y1, x2, y2) {
      return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    }
  
    // Triangle Area using Heron's Formula: √(s * (s - a) * (s - b) * (s - c)), where s = (a + b + c) / 2
    triangle_area_heron(a, b, c) {
      if (a < 0 || b < 0 || c < 0) throw new Error("Sides cannot be negative.");
      const s = (a + b + c) / 2;
      return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
  
    // Circle Circumference: 2 * π * r
    circle_circumference(radius) {
      return this.circumference_of_circle(radius); // Reuses the existing function
    }
  
    // Circle Area: π * r²
    circle_area(radius) {
      return this.area_of_circle(radius); // Reuses the existing function
    }
  
    // Parallelogram Area: b * h
    parallelogram_area(base, height) {
      if (base < 0 || height < 0) throw new Error("Base and height cannot be negative.");
      return base * height;
    }
  
    // Surface Area of a Sphere: 4 * π * r²
    sphere_surface_area(radius) {
      if (radius < 0) throw new Error("Radius cannot be negative.");
      return 4 * Math.PI * radius ** 2;
    }
  
    // Volume of a Sphere: (4/3) * π * r³
    sphere_volume(radius) {
      if (radius < 0) throw new Error("Radius cannot be negative.");
      return (4 / 3) * Math.PI * radius ** 3;
    }
  }
  