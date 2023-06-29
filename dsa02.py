def max_difference(arr):
    # Your code goes here
    pass

# Test the max_difference function
array = [4, 2, 9, 7, 5, 1, 6]
result = max_difference(array)
print("The maximum difference is:", result)


#ans

def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_element = arr[0]
    max_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]

    return max_diff

# Test the max_difference function
array = [4, 2, 9, 7, 5, 1, 6]
result = max_difference(array)
print("The maximum difference is:", result)



#The maximum difference is: 8
