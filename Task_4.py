# #TASK 1
# #your favourite quote
# quote = input("Please input your favourite quote: ")
# quotes = quote.title()
# print(f'\"{quotes}\"')

# #TASK 2 Shopping list master
# empty = []
# items = input("Enter 3 shopping items one by one with commas in between: ").split()
# empty = items.copy()
# print(empty)

# #Task 3 Word Counter
# sent = input("Enter a sentence: ")
# sent_list = list(sent.split()) #this converts the inputed sentence to list
# print(len(sent_list))

# # #Task 4 Name Organizer
# names = input("Enter five names separated by spaces: ").split()
# names = [name.lower() for name in names]
# print(*names ,sep="\n")

#OR
name = input("Enter five names separated by spaces: ").lower().split()
name.sort()
print(*name, sep="\n")

# #Task 5 Student Score Tracker
# list_name = []
# list_score = []

# name = input("Input three names: ").split()
# score = int(input("Enter the score for each student: "))
# list_name =name.copy()
# print(list_name)