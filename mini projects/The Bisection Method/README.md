# Bisection Method for Finding Square Roots

## Project Overview

This project implements the **bisection method** - a numerical algorithm for approximating square roots of numbers. The bisection method is a root-finding technique that iteratively narrows down the range of possible values until it converges on the solution.

## Purpose

This project demonstrates how the bisection method can be used to:

- Find square roots without using built-in functions
- Understand iterative approximation techniques
- Learn fundamental numerical analysis concepts

## How the Bisection Method Works

The bisection method finds the square root of a number `n` by:

1. **Setting an initial range**: Start with a lower bound (usually 0) and upper bound (the number itself, or a reasonable estimate)
2. **Finding the midpoint**: Calculate the middle value of the current range
3. **Testing the midpoint**: Square the midpoint and compare it to the target number
4. **Narrowing the range**: 
   - If midpoint² is too large, adjust the upper bound downward
   - If midpoint² is too small, adjust the lower bound upward
5. **Repeating**: Continue until the range is sufficiently narrow (desired precision is reached)

### Example: Finding √16

```
Initial range: [0, 16]
Iteration 1: midpoint = 8, 8² = 64 > 16 → new range [0, 8]
Iteration 2: midpoint = 4, 4² = 16 = 16 → found! √16 = 4
```
