# Subject: Data Structures and Algorithms

# Array Operations

# Initialize an array
array = [5, 2, 7, 1, 8]

# Access elements of an array
print("Array elements:")
for i in range(len(array)):
    print(array[i])

# Insert an element at a specific position
array.insert(2, 4)
print("Array after insertion:", array)

# Remove an element from the array
array.remove(7)
print("Array after removal:", array)

# Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Create a linked list
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(2)
linked_list.insert(7)
linked_list.insert(1)
linked_list.display()

# Dictionary Operations

# Create a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Access values in the dictionary
print("Name:", person["name"])
print("Age:", person.get("age"))

# Update values in the dictionary
person["age"] = 35
person["occupation"] = "Engineer"
print("Updated dictionary:", person)

# Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Searching Algorithms

# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test the sorting and searching algorithms
numbers = [5, 2, 7, 1, 8]
bubble_sort(numbers)
print("Sorted array (Bubble Sort):", numbers)

numbers = [5, 2, 7, 1, 8]
selection_sort(numbers)
print("Sorted array (Selection Sort):", numbers)

target = 7
index = binary_search(numbers, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")

