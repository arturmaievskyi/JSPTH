// File: MathUtils.ts

export class MathUtils {
    // Adds two numbers
    static add(a: number, b: number): number {
        return a + b;
    }

    // Subtracts the second number from the first
    static subtract(a: number, b: number): number {
        return a - b;
    }

    // Multiplies two numbers
    static multiply(a: number, b: number): number {
        return a * b;
    }

    // Divides the first number by the second
    // Throws an error if division by zero is attempted
    static divide(a: number, b: number): number {
        if (b === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return a / b;
    }

    // Finds the modulus (remainder) of the division of two numbers
    static modulus(a: number, b: number): number {
        return a % b;
    }

    // Calculates the power of a number (a^b)
    static power(base: number, exponent: number): number {
        return Math.pow(base, exponent);
    }

    // Returns the absolute value of a number
    static absolute(value: number): number {
        return Math.abs(value);
    }

    // Finds the square root of a number
    // Throws an error if the input is negative
    static squareRoot(value: number): number {
        if (value < 0) {
            throw new Error("Square root of negative numbers is not supported.");
        }
        return Math.sqrt(value);
    }

    // Rounds a number to the nearest integer
    static round(value: number): number {
        return Math.round(value);
    }

    // Generates a random number between two values (inclusive)
    static randomBetween(min: number, max: number): number {
        return Math.random() * (max - min) + min;
    }
}
