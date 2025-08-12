# #HOW TO CREATE A LIST
# #Method 1:Using square brackets
# empty_list =[]
# print(empty_list)

# #Method 2: Using the list() constructor
# empty_list2 = list()
# print(empty_list2)

# #Creating list with initial elements
# #List of integers
# num = [1,2,3,5]
# print(num)

# #List of strings
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# #Mixed data types
# mixed = ["Alice", 25, 5.8, True]
# print(mixed)

# #Creating a list from another sequence
# #From a string
# chars = list("hello")
# print(chars) #it prints each character of the string as an individual element in the list

# #From a tuple
# my_tuple = (10, 20, 30)
# list_from_tuple = list(my_tuple) #this converts the tuple to a list
# print(list_from_tuple) #this prints out the converted tuple in list format

# #From a range
# num_range = list(range(5)) #this converts the range of 0-4 to a list
# print(num_range) #this prints out the range in the form of a list

# #Using list comprehension
# squares = [x**2 for x in range(5)] #this creates a list containing the squares of the number in range 5 using a for loop
# print(squares) #this prints out squares of 0,1,2... in the format of a list

# evens = [x for x in range(11) if x % 2 == 0] #this creates a list of even numbers within the range of 11 using a combination of for loop and if statement
# print(evens)

# #Creating Nested list
# matrix = [[1,2,7], [3,4,8], [5,6,9]] #this creates a matrix like list
# print(matrix)
# #Indexing is used to access elements in a nested list
# print(f"{matrix[0]} \n{matrix[1]}")
# print(matrix[0][1]) #this feels like nested indexing, first it picks out the list with index number 0, then from the list with index number 0 it picks out the element with index number 1


# #CHARACTERISTICS OF A LIST
# #Ordered Collection
# fruits = ["mango", "orange", "banana"]
# print(fruits)
# print(fruits[0])
# print(fruits[2]) #basically explores the ordered nature of list, this prints out the element with the index number 2

# #Allows duplicates
# items = ["rice", "beans", "yam", "rice"]
# print(items)

# #Mutabe (can be changed)
# num = [1,2,3]
# num[1] = 20 #this changes the element with the index number 1
# print(num)

# #Can be nested
# nested_list = [[1,2], ["a","b"]]
# print(nested_list)
# print(nested_list[0][1])

#Dynamic size
name = ["Ada"]
name.append("Bola") #adds Bola to the variable currently containing Ada
name.append("Chidi") #add Chidi to the variable curretly containing Ada and Bola
print(name)