#TUPLE BASED QUESTION

# Question 11:
# Create a tuple with 5 different fruits and print the third fruit.

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("Third fruit:", fruits[2])  # Output: cherry

# Question 12:
# Convert the tuple (10, 20, 30, 40, 50) into a list,
# remove the number 30, and convert it back into a tuple.

numbers = (10, 20, 30, 40, 50)
numbers_list = list(numbers) #convert into a list
# Remove 30 from the list
numbers_list.remove(30)
updated_tuple = tuple(numbers_list)
print("Updated tuple:", updated_tuple)  # Output: (10, 20, 40, 50)

# Question 13:
# Try to append an element to the tuple (“A”, “B”, “C”).

letters = ("A", "B", "C")

# Tuples are immutable.
# Indirect method: convert tuple to list, modify, then convert back
letters_list = list(letters)
letters_list.append("D")
modified_tuple = tuple(letters_list)
print("Modified tuple:", modified_tuple)  # Output: ('A', 'B', 'C', 'D')


# Question 14:
# Unpack the tuple (100, 200, 300) into three separate variables and print them.

values = (100, 200, 300)

# Unpacking the tuple into variables
a, b, c = values

print("a:", a)  # Output: 100
print("b:", b)  # Output: 200
print("c:", c)  # Output: 300

# Question 15:
# Count the occurrences of 7 in the tuple (7, 1, 7, 3, 7, 5).

numbers = (7, 1, 7, 3, 7, 5)
# Using the count() method to find how many times 7 appears
count_sevens = numbers.count(7)
print("Number of times 7 appears:", count_sevens)  # Output: 3

