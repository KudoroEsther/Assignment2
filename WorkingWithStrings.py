# #single quotes
# name = 'Ada'

# #Double quotes
# greeting = "Hello"

# #Triple quotes (for multiline strings)
# story = '''Once upon a time,
# there was a coder named Esther'''

# #String with numbers and symbols
# password ="p@ssw0rd123"

# #STRING OPERATIONS
# #INDEXING
# word ="Python"
# print(word[0]) #This should print out the first character in the variable named word
# print(word[-1]) #This should print out the last character

#Slicing
# word = "A string in Python is a sequence of characters enclosed in either single quotes\
# , double quotes or triple quotes. Strings are used to store text data like names, \
# sentences, or any combination of letters, numbers, and symbols."
# print(f"{word[0:10]}\n") #prints out the characters from index 0 to 10
# print(f"{word[5:]}\n") #prints out the character from index 5 to the end
# print(f"{word[:110]}\n") #prints out the characters and stops at index 110
# print(f"{word[::2]}\n") #Prints out all the characters with a step size of two
# print(f"{word[::-1]}\n") #Prints out all the characters backwards with a step size of 1

#STRING CONCATENATION & REPETITION
#Concatenation
# a = "Hello"
# b = "Word"
# print(a + " " +b) #prints out Hello world

# #Repetition
# word = "Hi! "
# print(word*3) #Prints the content of the variable named word thrice

#STRING SEARCHING & CHECKING
#Membership
# text = "Python Programming Java"
# print("Python" in text ) #checks if the strings exist in the variable and prints True or False
# print("Java" not in text) #checks that the string doesn't exist in the variable and prints True or False

# #find() / rfind()
# text = "Hello world today is good"
# print(text.find("o")) #returns the first index of the string defined in the case "o"
# print(text.rfind("o")) #returns the last index of the string defined in this cas4e "o"

# #startswith() / endswith 
# filename = "data.csv"
# print(filename.startswith("data")) #this checks if the specified string is at the beginning of the variable's content
# print(filename.endswith(".csv"))#this checks if the specified string is at the end of the variable's content. It returns True or False
