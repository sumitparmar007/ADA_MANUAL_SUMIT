def find_factorial(n):
# Base condition
if n <= 1:
return 1
# Recursive call
return n * find_factorial(n - 1)

# Example
num2 = 6
print("Factorial using recursion:", find_factorial(num2))