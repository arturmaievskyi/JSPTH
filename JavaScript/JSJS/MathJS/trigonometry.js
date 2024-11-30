class Trigonometry {
    constructor() {
      this.radiansToDegrees = (rad) => rad * (180 / Math.PI);
      this.degreesToRadians = (deg) => deg * (Math.PI / 180);
    }
  
    // Basic Trigonometric Functions
    sine(angle) {
      return Math.sin(angle);
    }
  
    cosine(angle) {
      return Math.cos(angle);
    }
  
    tangent(angle) {
      return Math.tan(angle);
    }
  
    arcsine(value) {
      return Math.asin(value);
    }
  
    arccosine(value) {
      return Math.acos(value);
    }
  
    arctangent(value) {
      return Math.atan(value);
    }
  
    // Reciprocal Trigonometric Functions
    secant(angle) {
      return 1 / Math.cos(angle);
    }
  
    cosecant(angle) {
      return 1 / Math.sin(angle);
    }
  
    cotangent(angle) {
      return 1 / Math.tan(angle);
    }
  
    // Law of Cosines
    law_of_cosines(a, b, c) {
      return Math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b));
    }
  
    // Law of Sines
    law_of_sines(opposite, hypotenuse, angle) {
      return opposite / Math.sin(angle) === hypotenuse / Math.sin(Math.PI - angle);
    }
  
    // Sum and Double-Angle Identities
    sine_sum(a, b) {
      return this.sine(a) * this.cosine(b) + this.cosine(a) * this.sine(b);
    }
  
    cosine_sum(a, b) {
      return this.cosine(a) * this.cosine(b) - this.sine(a) * this.sine(b);
    }
  
    tangent_sum(a, b) {
      return (this.tangent(a) + this.tangent(b)) / (1 - this.tangent(a) * this.tangent(b));
    }
  
    sine_double(a) {
      return 2 * this.sine(a) * this.cosine(a);
    }
  
    cosine_double(a) {
      return this.cosine(a) ** 2 - this.sine(a) ** 2;
    }
  
    tangent_double(a) {
      return (2 * this.tangent(a)) / (1 - this.tangent(a) ** 2);
    }
  
    // Coordinate Conversions
    polar_to_cartesian(r, theta) {
      return {
        x: r * this.cosine(theta),
        y: r * this.sine(theta),
      };
    }
  
    cartesian_to_polar(x, y) {
      return {
        r: Math.sqrt(x ** 2 + y ** 2),
        theta: Math.atan2(y, x),
      };
    }
  }
  