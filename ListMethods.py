# #LIST METHODS
# #.append() method
# fruits = ["apple", "banana"]
# fruits.append(["cherry"]) #adds the list cherry to the list called fruits
# print(fruits)

# #.insert() method
# fruits = ["apple", "banana"]
# fruits.insert(0, "orange") #inserts orange at the specified index number
# print(fruits)

# #.extend() method
# fruits = ["apple", "banana"]
# tropical = ["mango", "pineapple"]
# fruits.extend(tropical) #add the content of the list called tropical to the end of list called fruits.
# print(fruits)

# #.remove() method
# fruits = ["apple", "banana", "cherry", "banana"]
# fruits.remove("banana") #removes the first occurrence of banana in the list
# print(fruits)

# #.pop() method
# fruits = ["apple","banana", "cherry"]
# last_fruit = fruits.pop()
# print(last_fruit) #prints out the element in the list
# print(fruits) #prints out the list without the last element since it has been removed

# #.clear() method
# fruits = ["apple","banana", "cherry"]
# fruits.clear() #this prints out an empty list
# print(fruits)

# #.index() method
# fruits = ["apple","banana", "cherry"]
# position = fruits.index("cherry") #this is used to obtain the index number of the specified element
# print(position)

# #.count() method
# fruits = ["apple","banana", "cherry", "banana"]
# print(fruits.count("banana")) #counts how many times banana appears in the list

#.sort() method
nums = [3,2,4,6]
nums.sort() #sorts the list in ascending order. Works for strings too
print(nums)

#descending order
nums.sort(reverse=True) #sorts the list in descending order
print(nums)

#.reverse() method
fruits = ["apple","banana", "cherry"]
fruits.reverse() #reverses the order of the string
print(fruits)

#.copy()
fruits = ["apple","banana", "cherry"]
new = fruits.copy()
print(new) #copies the content of fruits into list