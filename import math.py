import math

def D_math_function(a, b, c):
    discriminant = (b**2) - (4*a*c)
    
    if discriminant < 0:
        return "No real solution"
    elif discriminant == 0:
        x = (-b) / (2*a)
        return "One real solution: {}".format(x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Two real solutions: {} and {}".format(x1, x2)

# Example usage:
a = 1
b = 3
c = 2
print(D_math_function(a, b, c)) # Output: "Two real solutions: 1.0 and 2.0"