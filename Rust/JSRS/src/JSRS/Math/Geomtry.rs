use std::f64::consts::PI;

struct GeometrySolver;

impl GeometrySolver {
    /// Computes the area of a circle given its radius.
    fn area_of_circle(radius: f64) -> f64 {
        PI * radius * radius
    }

    /// Computes the circumference of a circle given its radius.
    fn circumference_of_circle(radius: f64) -> f64 {
        2.0 * PI * radius
    }

    /// Computes the volume of a cone given its radius and height.
    fn volume_of_cone(radius: f64, height: f64) -> f64 {
        (PI * radius * radius * height) / 3.0
    }

    /// Computes the surface area of a cone given its radius and slant height.
    fn surface_area_of_cone(radius: f64, slant_height: f64) -> f64 {
        PI * radius * (radius + slant_height)
    }

    /// Computes the distance between two points in 2D space.
    fn distance_between_points(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
        ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt()
    }

    /// Computes the area of a triangle using Heron's formula.
    fn triangle_area_heron(a: f64, b: f64, c: f64) -> Result<f64, &'static str> {
        if a + b <= c || a + c <= b || b + c <= a {
            return Err("Invalid triangle sides.");
        }
        let s = (a + b + c) / 2.0;
        Ok((s * (s - a) * (s - b) * (s - c)).sqrt())
    }

    /// Computes the area of a parallelogram given its base and height.
    fn parallelogram_area(base: f64, height: f64) -> f64 {
        base * height
    }

    /// Computes the surface area of a sphere given its radius.
    fn sphere_surface_area(radius: f64) -> f64 {
        4.0 * PI * radius * radius
    }

    /// Computes the volume of a sphere given its radius.
    fn sphere_volume(radius: f64) -> f64 {
        (4.0 / 3.0) * PI * radius.powi(3)
    }
}