# Subject: Practice with Loops and Conditional Statements

# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Calculate the sum of numbers from 1 to 100
sum_result = 0
for i in range(1, 101):
    sum_result += i
print("Sum:", sum_result)

# Find the largest number in a list
numbers = [5, 8, 2, 11, 3]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print("Max number:", max_number)

# Print the Fibonacci sequence up to the n-th term
n = 10
fib_sequence = [0, 1]
while len(fib_sequence) < n:
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)
print("Fibonacci sequence:", fib_sequence)

# Check if a number is prime
number = 17
is_prime = True
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
print("Is prime:", is_prime)

# Generate a multiplication table
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end="\t")
    print()

# Calculate the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
factorial_result = factorial(num)
print(f"Factorial of {num}: {factorial_result}")
