# #LIST OPERATIONS IN PYTHON
# #Concatenation (+) Joins two lists into a new list
# list1 = [1,2,3]
# list2 = [3,4,5,6]
# result = list1 + list2 #This combines the two lists, it doesn't perform the mathematical addition
# print(result)
# print(list1 + list2) #Does the same thing as concatenating and saving in a variable

# #Repetition
# nums = [2,3]
# repeat = nums*3 #this duplicates the content of the variable thrice. Quite similar to what string does
# print(repeat)

# #Indexing
# fruit = ["apple", "banana", "pawpaw", "cherry"]
# print(fruit[1][1:])
# print(fruit[-2][3:]) # this is slicing within indexing. prints out the characters from index 3 downwards from the list element with index number -2 in this case (paw from pawpaw)

#Slicing
numbers = [1,2,3,4,5,6]
print(numbers[1:4]) #Same function as in string
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

#Membership (in/not in)
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

#Length (len())
items = ["pen", "book", "laptop"]
print(len(items)) #prints the number of elements in a list, in this case 3

#min and max (min()/max())
nums = [5,2,9,1]
print(min(nums))
print(max(nums))

#Sum()
numbers = [1,2,3,70]
print(sum(numbers))

#List comprehension
squares = [x**2 for x in range(5)]
print(squares)

#Copying a List
a = [1,2,4]
b = a.copy() #this copies the content of a into b
print(b)