# ADVANCED PROBLEMS:
# Question 16:
# Write a function that takes a list and returns a new list with all even numbers removed.

def remove_even_numbers(input_list):
    return [num for num in input_list if num % 2 != 0]
nums = [1, 2, 3, 4, 5, 6]
print("List with even numbers removed:", remove_even_numbers(nums))  # Output: [1, 3, 5]


# Question 17:
# Create a function that accepts a list and returns a new list with elements sorted in
# descending order without using the sort() method.

def sort_descending(input_list):
    return sorted(input_list, reverse=True)

unsorted_list = [4, 1, 7, 3, 9]
print("Sorted in descending order:", sort_descending(unsorted_list))  # Output: [9, 7, 4, 3, 1]

# Question 18:
# Given a list of numbers, write a program to remove all duplicate elements and print the unique elements.

def remove_duplicates(input_list):
    # Converting to set removes duplicates, then convert back to list
    return list(set(input_list))

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5] (order may vary)


# Question 19:
# Given a tuple of names (“Alice”, “Bob”, “Charlie”, “Alice”, “David”), convert
# it into a list, remove duplicates, and convert it back to a tuple.

names_tuple = ("Alice", "Bob", "Charlie", "Alice", "David")

# Convert to list
names_list = list(names_tuple)

# Remove duplicates using set, then back to list and tuple
unique_names = list(set(names_list))
unique_names_tuple = tuple(unique_names)

print("Tuple with duplicates removed:", unique_names_tuple)
# Output could be in any order, like ('Charlie', 'Bob', 'David', 'Alice')


# Question 20:
# Create a program that takes a list of mixed data types (int, str, float) and separates
# integers into one list, strings into another, and floats into another.

def separate_data_types(mixed_list):
    ints = []
    strs = []
    floats = []
    
    for item in mixed_list:
        if isinstance(item, int):
            ints.append(item)
        elif isinstance(item, str):
            strs.append(item)
        elif isinstance(item, float):
            floats.append(item)
    
    return ints, strs, floats


mixed = [1, "hello", 2.5, 3, "world", 4.0, 7]
int_list, str_list, float_list = separate_data_types(mixed)

print("Integers:", int_list)    # Output: [1, 3, 7]
print("Strings:", str_list)     # Output: ['hello', 'world']
print("Floats:", float_list)    # Output: [2.5, 4.0]
