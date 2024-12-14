// File: GeometryUtils.ts

export class GeometryUtils {
    // Area of a Circle
    static areaOfCircle(radius: number): number {
        return Math.PI * radius ** 2;
    }

    // Circumference of a Circle
    static circumferenceOfCircle(radius: number): number {
        return 2 * Math.PI * radius;
    }

    // Volume of a Cone
    static volumeOfCone(radius: number, height: number): number {
        return (1 / 3) * Math.PI * radius ** 2 * height;
    }

    // Surface Area of a Cone
    static surfaceAreaOfCone(radius: number, slantHeight: number): number {
        return Math.PI * radius * (radius + slantHeight);
    }

    // Distance Between Two Points in 2D space
    static distanceBetweenPoints(x1: number, y1: number, x2: number, y2: number): number {
        return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    }

    // Area of a Triangle using Heron's Formula
    static triangleAreaHeron(a: number, b: number, c: number): number {
        const s = (a + b + c) / 2; // Semi-perimeter
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }

    // Area of a Parallelogram
    static parallelogramArea(base: number, height: number): number {
        return base * height;
    }

    // Surface Area of a Sphere
    static sphereSurfaceArea(radius: number): number {
        return 4 * Math.PI * radius ** 2;
    }

    // Volume of a Sphere
    static sphereVolume(radius: number): number {
        return (4 / 3) * Math.PI * radius ** 3;
    }

    // Circle Circumference (alias of circumferenceOfCircle)
    static circleCircumference(radius: number): number {
        return GeometryUtils.circumferenceOfCircle(radius);
    }

    // Circle Area (alias of areaOfCircle)
    static circleArea(radius: number): number {
        return GeometryUtils.areaOfCircle(radius);
    }
}
