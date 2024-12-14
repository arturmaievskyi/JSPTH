export class Trigonometry {
    // Basic Trigonometric Functions
    static sine(angle: number): number {
        return Math.sin(angle);
    }

    static cosine(angle: number): number {
        return Math.cos(angle);
    }

    static tangent(angle: number): number {
        if (Math.cos(angle) === 0) {
            throw new Error("Tangent undefined for angles where cos(angle) = 0.");
        }
        return Math.tan(angle);
    }

    // Inverse Trigonometric Functions
    static arcsine(value: number): number {
        if (value < -1 || value > 1) {
            throw new Error("Input for arcsine must be between -1 and 1.");
        }
        return Math.asin(value);
    }

    static arccosine(value: number): number {
        if (value < -1 || value > 1) {
            throw new Error("Input for arccosine must be between -1 and 1.");
        }
        return Math.acos(value);
    }

    static arctangent(value: number): number {
        return Math.atan(value);
    }

    // Reciprocal Trigonometric Functions
    static secant(angle: number): number {
        const cos = Math.cos(angle);
        if (cos === 0) {
            throw new Error("Secant undefined for angles where cos(angle) = 0.");
        }
        return 1 / cos;
    }

    static cosecant(angle: number): number {
        const sin = Math.sin(angle);
        if (sin === 0) {
            throw new Error("Cosecant undefined for angles where sin(angle) = 0.");
        }
        return 1 / sin;
    }

    static cotangent(angle: number): number {
        const tan = Math.tan(angle);
        if (tan === 0) {
            throw new Error("Cotangent undefined for angles where tan(angle) = 0.");
        }
        return 1 / tan;
    }

    // Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(C)
    static lawOfCosines(a: number, b: number, angleC: number): number {
        return Math.sqrt(a ** 2 + b ** 2 - 2 * a * b * Math.cos(angleC));
    }

    // Law of Sines: a/sin(A) = b/sin(B) = c/sin(C)
    static lawOfSines(side: number, angle: number, otherAngle: number): number {
        return (side * Math.sin(otherAngle)) / Math.sin(angle);
    }

    // Angle Sum Formulas
    static sineSum(angleA: number, angleB: number): number {
        return Math.sin(angleA) * Math.cos(angleB) + Math.cos(angleA) * Math.sin(angleB);
    }

    static cosineSum(angleA: number, angleB: number): number {
        return Math.cos(angleA) * Math.cos(angleB) - Math.sin(angleA) * Math.sin(angleB);
    }

    static tangentSum(angleA: number, angleB: number): number {
        const denominator = 1 - Math.tan(angleA) * Math.tan(angleB);
        if (denominator === 0) {
            throw new Error("Tangent sum undefined when tan(angleA) * tan(angleB) = 1.");
        }
        return (Math.tan(angleA) + Math.tan(angleB)) / denominator;
    }

    // Double Angle Formulas
    static sineDouble(angle: number): number {
        return 2 * Math.sin(angle) * Math.cos(angle);
    }

    static cosineDouble(angle: number): number {
        return Math.cos(angle) ** 2 - Math.sin(angle) ** 2;
    }

    static tangentDouble(angle: number): number {
        const denominator = 1 - Math.tan(angle) ** 2;
        if (denominator === 0) {
            throw new Error("Tangent double-angle undefined when tan(angle)^2 = 1.");
        }
        return 2 * Math.tan(angle) / denominator;
    }

    // Coordinate Conversion
    static polarToCartesian(radius: number, angle: number): { x: number; y: number } {
        return {
            x: radius * Math.cos(angle),
            y: radius * Math.sin(angle),
        };
    }

    static cartesianToPolar(x: number, y: number): { radius: number; angle: number } {
        return {
            radius: Math.sqrt(x ** 2 + y ** 2),
            angle: Math.atan2(y, x),
        };
    }
}