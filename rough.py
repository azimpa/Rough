# unique elements
def find_unique_elements(arr):
    unique_elements = set()
    for element in arr:
        unique_elements.add(element)
    return list(unique_elements)


my_array = [1, 2, 3, 4, 1, 2, 5, 6, 3, 4, 7, 8, 5]
unique_elements = find_unique_elements(my_array)
print("Unique elements:", unique_elements)


# reversing elements
def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]


# reversing string
def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string


s = "hello"
reversed_s = reverse_string(s)
print(reversed_s)  # Output: "olleh"


# Recursion factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


result = factorial_recursive(7)
print(result)


# Recursion fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence


n = 10
fib_seq = fibonacci(n)
print(fib_seq)

# Valid Anagram


def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of both strings are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings and compare them
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"

if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


# by using hashmap
def is_anagram(str1, str2):
    # Check if lengths of both strings are equal
    if len(str1) != len(str2):
        return False

    # Create a hashmap to store character counts
    char_count = {}

    # Count occurrences of characters in str1
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement count for characters in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            # If a character in str2 is not in str1, they can't be anagrams
            return False

    # Check if all character counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    # If all conditions are satisfied, strings are anagrams
    return True


print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))  # Output: False


# missing number
def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number


# Example usage
numbers = [1, 2, 4, 5, 6]  # Missing number: 3
missing_number = find_missing_number(numbers)
print("Missing number is:", missing_number)


# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
# Swapping keys and values
swapped_dict = {value: key for key, value in original_dict.items()}
print(swapped_dict)


# Removing duplicates from a list without using a new list
def remove_duplicates(lst):
    seen = set()
    i = 0
    while i < len(lst):
        if lst[i] in seen:
            lst.pop(i)
        else:
            seen.add(lst[i])
            i += 1


# Example usage
my_list = [1, 2, 3, 2, 1, 4, 5, 3]
remove_duplicates(my_list)
print(my_list)

# remove_duplicates


def remove_duplicates(lst):
    i = 0
    while i < len(lst):
        if lst.count(lst[i]) > 1:
            lst.remove(lst[i])
        else:
            i += 1


# Example
my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
remove_duplicates(my_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


# binary_search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")


# binary search using recursion
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


arr = [10, 20, 30, 40, 50]
target = 60
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")


# linear_search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4

position = linear_search(arr, target)

if position != -1:
    print("Value found at position", position + 1)
else:
    print("Value not found")


# bubble_sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


# insertion_sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)


# merge_sort
def merge(l, r):
    result = []  # This will hold the merged sorted elements
    i, j = 0, 0  # Pointers to keep track of current indices in l and r

    while i < len(l) and j < len(r):  # Loop through both arrays until one is exhausted
        if l[i] < r[j]:  # Compare elements at the current indices of l and r
            result.append(l[i])  # Add the smaller element to the result
            i += 1  # Move to the next element in l
        else:
            result.append(r[j])  # Add the smaller element to the result
            j += 1  # Move to the next element in r
    # At this point, one of the arrays is exhausted # Append any remaining elements from l or r to the result
    result.extend(l[i:])  # Add remaining elements of l (if any)
    result.extend(r[j:])  # Add remaining elements of r (if any)
    return result  # Return the merged sorted array


def merge_sort(arr):  # Function to perform merge sort on an array
    if len(arr) <= 1:  # Base case: if the array has 0 or 1 elements, it is already sorted
        return arr

    # Find the midpoint to divide the array into two halves
    mid = len(arr) // 2
    l = merge_sort(arr[:mid])      # Recursively sort the left half
    r = merge_sort(arr[mid:])      # Recursively sort the right half

    return merge(l, r)      # Merge the sorted halves


array = [9, 5, 1, 3, 8, 4, 2, 7, 6]
sorted_array = merge_sort(array)
print(sorted_array)


# quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)


# selection_sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# merge sorted
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
result = merge_sorted_arrays(arr1, arr2)
print(result)


# Sum of array using recursion
def sum_array(arr):
    if not arr:
        return 0
    # Recursive case: add the first element to the sum of the rest of the array
    else:
        return arr[0] + sum_array(arr[1:])


my_array = [1, 2, 3, 4, 5]
print("Sum of array:", sum_array(my_array))  # Output: Sum of array: 15
