def factorial(n):
    # Your code goes here
    pass

# Test the factorial function
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")



# ans

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Test the factorial function
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
