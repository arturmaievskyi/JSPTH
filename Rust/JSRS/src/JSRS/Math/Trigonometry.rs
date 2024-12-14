// src/main.rs

use std::f64::consts::PI;

struct TrigonometrySolver;

impl TrigonometrySolver {
    /// Converts degrees to radians.
    fn to_radians(degrees: f64) -> f64 {
        degrees * PI / 180.0
    }

    /// Converts radians to degrees.
    fn to_degrees(radians: f64) -> f64 {
        radians * 180.0 / PI
    }

    /// Basic trigonometric functions
    fn sine(angle: f64) -> f64 {
        angle.sin()
    }

    fn cosine(angle: f64) -> f64 {
        angle.cos()
    }

    fn tangent(angle: f64) -> f64 {
        angle.tan()
    }

    fn secant(angle: f64) -> f64 {
        1.0 / angle.cos()
    }

    fn cosecant(angle: f64) -> f64 {
        1.0 / angle.sin()
    }

    fn cotangent(angle: f64) -> f64 {
        1.0 / angle.tan()
    }

    /// Inverse trigonometric functions
    fn arcsine(value: f64) -> f64 {
        value.asin()
    }

    fn arccosine(value: f64) -> f64 {
        value.acos()
    }

    fn arctangent(value: f64) -> f64 {
        value.atan()
    }

    /// Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(C)
    fn law_of_cosines(a: f64, b: f64, angle_c: f64) -> f64 {
        (a.powi(2) + b.powi(2) - 2.0 * a * b * angle_c.cos()).sqrt()
    }

    /// Law of Sines: a / sin(A) = b / sin(B) = c / sin(C)
    fn law_of_sines(a: f64, angle_a: f64, angle_b: f64) -> f64 {
        a * angle_b.sin() / angle_a.sin()
    }

    /// Angle sum and double angle formulas
    fn sine_sum(angle1: f64, angle2: f64) -> f64 {
        angle1.sin() * angle2.cos() + angle1.cos() * angle2.sin()
    }

    fn cosine_sum(angle1: f64, angle2: f64) -> f64 {
        angle1.cos() * angle2.cos() - angle1.sin() * angle2.sin()
    }

    fn tangent_sum(angle1: f64, angle2: f64) -> f64 {
        (angle1.tan() + angle2.tan()) / (1.0 - angle1.tan() * angle2.tan())
    }

    fn sine_double(angle: f64) -> f64 {
        2.0 * angle.sin() * angle.cos()
    }

    fn cosine_double(angle: f64) -> f64 {
        1.0 - 2.0 * angle.sin().powi(2)
    }

    fn tangent_double(angle: f64) -> f64 {
        2.0 * angle.tan() / (1.0 - angle.tan().powi(2))
    }

    /// Polar to Cartesian coordinates conversion
    fn polar_to_cartesian(radius: f64, angle: f64) -> (f64, f64) {
        let x = radius * angle.cos();
        let y = radius * angle.sin();
        (x, y)
    }

    /// Cartesian to Polar coordinates conversion
    fn cartesian_to_polar(x: f64, y: f64) -> (f64, f64) {
        let radius = (x.powi(2) + y.powi(2)).sqrt();
        let angle = y.atan2(x);
        (radius, angle)
    }
}
