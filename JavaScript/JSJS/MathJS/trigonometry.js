class Trigonometry {
    sine(x) {
        return Math.sin(x);
    }

    cosine(x) {
        return Math.cos(x);
    }

    tangent(x) {
        return Math.tan(x);
    }

    secant(x) {
        if (Math.cos(x) === 0) throw new Error("Secant undefined at this angle");
        return 1 / Math.cos(x);
    }

    cosecant(x) {
        if (Math.sin(x) === 0) throw new Error("Cosecant undefined at this angle");
        return 1 / Math.sin(x);
    }

    cotangent(x) {
        if (Math.tan(x) === 0) throw new Error("Cotangent undefined at this angle");
        return 1 / Math.tan(x);
    }
    arcsine(x) {
        return Math.asin(x);
    }

    arccosine(x) {
        return Math.acos(x);
    }

    arctangent(x) {
        return Math.atan(x);
    }

    law_of_cosines(a, b, angleC) {
        return Math.sqrt(a * a + b * b - 2 * a * b * Math.cos(angleC));
    }

    law_of_sines(a, angleA, angleB) {
        return (a * Math.sin(angleB)) / Math.sin(angleA);
    }

    sine_sum(x, y) {
        return Math.sin(x) * Math.cos(y) + Math.cos(x) * Math.sin(y);
    }

    cosine_sum(x, y) {
        return Math.cos(x) * Math.cos(y) - Math.sin(x) * Math.sin(y);
    }

    tangent_sum(x, y) {
        if (Math.cos(x) * Math.cos(y) === 0) throw new Error("Tangent sum undefined for these angles");
        return (Math.tan(x) + Math.tan(y)) / (1 - Math.tan(x) * Math.tan(y));
    }


    sine_double(x) {
        return 2 * Math.sin(x) * Math.cos(x);
    }

    cosine_double(x) {
        return Math.cos(x) * Math.cos(x) - Math.sin(x) * Math.sin(x);
    }

    tangent_double(x) {
        if (Math.cos(x) * Math.cos(x) === 0) throw new Error("Tangent double undefined for this angle");
        return (2 * Math.tan(x)) / (1 - Math.tan(x) * Math.tan(x));
    }

    polar_to_cartesian(radius, angle) {
        return {
            x: radius * Math.cos(angle),
            y: radius * Math.sin(angle),
        };
    }

    cartesian_to_polar(x, y) {
        return {
            radius: Math.sqrt(x * x + y * y),
            angle: Math.atan2(y, x),
        };
    }
}