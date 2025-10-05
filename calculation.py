import math

def calculate_with_math_module(number):
    print("---- Calculations using math module ----")
    print(f"Square Root of {number}: {math.sqrt(number):.2f}")
    print(f"Logarithm of {number}: {math.log(number):.4f}")
    print(f"Sine of {number} (in radians): {math.sin(number):.4f}")
num = float(input("Enter a number: "))
calculate_with_math_module(num)