# Subject: Mathematical Operations

# Calculate the sum of numbers from 1 to 100
sum_result = sum(range(1, 101))
print("Sum:", sum_result)

# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
factorial_result = factorial(num)
print(f"Factorial of {num}: {factorial_result}")


# Subject: File Handling

# Read contents from a text file
with open('sample.txt', 'r') as file:
    contents = file.read()
    print("File contents:", contents)

# Write contents to a text file
data = "Hello, World!"
with open('output.txt', 'w') as file:
    file.write(data)
    print("Data written to file.")


# Subject: String Manipulation

# Reverse a string
def reverse_string(s):
    return s[::-1]

string = "Hello, World!"
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)

# Count the occurrences of a substring in a string
def count_substring(string, substring):
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += len(substring)
    return count

string = "Hello, Hello, Hello"
substring = "Hello"
occurrences = count_substring(string, substring)
print(f"Occurrences of '{substring}': {occurrences}")


# Subject: Data Structures

# Create a list and perform various operations
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)

fruits.append("grape")
print("Fruits (after append):", fruits)

fruits.remove("banana")
print("Fruits (after remove):", fruits)

fruit_index = fruits.index("orange")
print("Index of 'orange':", fruit_index)

# Create a dictionary and perform various operations
person = {"name": "John", "age": 30, "city": "New York"}
print("Person:", person)

person["occupation"] = "Engineer"
print("Person (after adding occupation):", person)

person.pop("age")
print("Person (after removing age):", person)


# Subject: Error Handling

# Handle division by zero exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Subject: API Integration

import requests

# Make a GET request to an API
response = requests.get("https://api.example.com/data")
data = response.json()
print("API response:", data)


# Subject: Concurrency

import threading

# Define a function to be executed in a separate thread
def worker():
    print("Worker thread executing...")

# Create and start a new thread
thread = threading.Thread(target=worker)
thread.start()
print("Main thread continues...")


# Subject: Data Analysis

import pandas as pd

# Load data from a CSV file
data = pd.read_csv("data.csv")

# Perform data analysis tasks
# ...


# Subject: Web Scraping

import requests
from bs4 import BeautifulSoup

# Make a request to a web page
response = requests.get("https://www.example.com")
html_content = response.text

# Parse HTML and extract information
soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string
print("Web page title:", title)


# Subject: Machine Learning

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load a dataset
boston = datasets.load_boston()
X = boston.data
y = boston.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)
print("Predictions:", predictions)

