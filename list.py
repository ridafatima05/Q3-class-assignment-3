#BASIC LIST OPERATIONS:

# Q1: CREATE A LIST OF FIVE NUMBERS AND APPEND A NEW NUMBER TO IT. PRINT THE UPDATED LIST:
 
list1 : list = [1,2,3,4,5]
list1.append(6)
print(list1)

# Q2: EXTEND A LIST [1,2,3] WITH ANOTHER LIST [4,5,6] PRINT THE RESULT.
list2 : list = [1,2,3]
list2.extend([4,5,6])
print(list2)

# Q3: INSERT THE STRING "Python" at index 2 in the list ["Java", "C++", "JavaScript", "Ruby"]. 

computer_lang = ["Java", "C++", "JavaScript", "Ruby"]
computer_lang.insert(2,"Python")
print(computer_lang)

# Q4: Remove the first occurrence of the number 10 from the list [10, 20, 30, 10, 40]. 

numbers = [10, 20, 30, 10, 40]
numbers.remove(10)  # Removes the first 10 it finds!
print(numbers)

# Q5: Use the pop() method to remove the last element from [100, 200, 300, 400] and 
#     print the modified list.

num_list = [100,200,300,400]
num_list.pop()  
print(num_list)

# INTERMEDIATE LIST OPERATIONS:

# Q6: Count how many times the number 5 appears in the list [5, 10, 5, 20, 5, 30]. 

numbers = [5, 10, 5, 20, 5, 30]
count_5 = numbers.count(5)     #store in variable then print 
print("Number 5 appears", count_5, "times.")


# Q7: Sort the list [9, 1, 8, 3, 5] in ascending and descending order. 

numbers = [9, 1, 8, 3, 5]

# Ascending order
ascending = sorted(numbers)
print("Ascending:", ascending) #1,3,5,8,9

# Descending order
descending = sorted(numbers, reverse=True) #9,8,5,3,1
print("Descending:", descending)

#KEY POINTS:
#.sort() modifies the list in place and doesn't return anything. only works on list
# sorted() returns a new sorted list and does not modify the original list.


# Q8: Reverse the list [“apple”, “banana”, “cherry”] using the reverse() method. 

#.reverse() modifies the list directly, reversing the order of elements.
fruits = ["Apple","Banana","Cherry"]
fruits.reverse()
print(fruits)

# Q9: Create a copy of the list [1, 2, 3, 4, 5] and store it in another variable.
# Modify the copied list and print both lists. 

original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()

copied_list.append(6) #modified list

print("Original list:", original_list)
print("Copied list:", copied_list)


# Q10:  Clear all elements from a list [“hello”, “world”, “python”] using the clear() method.
 
friends_list = ["Aina", "Shifa", "Ifza","Aiman"]
print(f"List Before using clear() function:{friends_list}")
friends_list.clear()
print(f"List after using Clear() function : {friends_list}")

