export class Calculator {
    add(a, b) {
      return a + b;
    }
  
    subtract(a, b) {
      return a - b;
    }
  
    multiply(a, b) {
      return a * b;
    }
  
    divide(a, b) {
      if (b === 0) {
        throw new Error("Cannot divide by zero");
      }
      return a / b;
    }
  
    factorial(n) {
      if (n < 0) {
        throw new Error("Factorial is not defined for negative numbers");
      }
      if (n === 0 || n === 1) {
        return 1;
      }
      let result = 1;
      for (let i = 2; i <= n; i++) {
        result *= i;
      }
      return result;
    }
  
    square(n) {
      return n * n;
    }
  
    root(n) {
      if (n < 0) {
        throw new Error("Cannot take the square root of a negative number");
      }
      return Math.sqrt(n);
    }
}

