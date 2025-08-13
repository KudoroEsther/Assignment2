# #CREATING SETS 
# #Using curly braces
# fruits = {"apple", "banana", "mango"}
# print(fruits)

# #using set constructor
# nums = set([1,2,3,4]) #set() only accepts one argument, the square bracket is needed to act as a single argument
# print(nums)

# #Creating an empty set (must use set() not {})
# #I used empty_set = {} and it worked
# empty_set = set()
# print(empty_set)

# #From a string
# letters = set("mississippi") #removes all duplicates
# print(letters)


# #SET OPERATIONS
# #Adding elements
# colors = {"red", "blue"}
# colors.add("green") #works like append in list
# print(colors)

# #Removing elements
# colors.remove("blue") #will raise error if blue is not found
# colors.discard("yellow") #will not raise error if yellow is not found
# print(colors)

# #Pop an element
# colors = {"red", "blue", "green"}
# removed = colors.pop()
# print("Removed:", removed) #prints the last element in the set
# print("Remaining:", colors) 

# #Clear a set
# colors.clear()
# print(colors) #prints an empty set\


# #MATHEMATICAL SET OPERATIONS
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# #Union
# print(set1|set2) #combines set1 and set2 whilst removing duplicates

# #Intersection
# print(set1 & set2) #prints the common elements in set1 and set2
# print(set1.intersection(set2))

# #Difference
# print(set1 - set2) #prints the elements that can be found in set 1 but not set2
# print(set2.difference(set1)) #prints the elements that can be found in set2 but not set1

# #Symmetric difference
# print(set1^set2) #removes the common characters in both sets and combines the sets
# print(set1.symmetric_difference(set2))


#WORKING WITH SETS
#Collecting unique visitor to an event
visitors = set()
#Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") #this is ignore since it Chinedu is a duplicate
print("Visitors:", visitors)

#checking if a visitor attended
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")