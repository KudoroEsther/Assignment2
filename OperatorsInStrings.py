#upper()
name ="Ada Balogun"
print(name.upper())#this prints out name in uppercase

#title()
sentence = "python is amazing"
print(sentence.title()) #prints out sentence in title case

#lower()
sentencee = "PYTHON IS AMAZING"
print(sentencee.lower()) #prints out the variable's content in lowercase

#strip() Remove whitespace or specified characters from both ends of the string
text = " ABUJA "
print(text.strip())

#replace()
message = "I love Java"
print(message.replace("Java", "Python")) #this replaces java with python

#swapcase
text = "HELLO abeokuta"
print(text.swapcase()) #swaps uppercase to lowercase and vice versa

#lstrip() removes whitespace or specified characters from the left side only
text = " Nigeria is green"
print(text.lstrip())

#rstrip() removes whitespace or specified characters from the left side only
text = " Nigeria "
print(text.rstrip())

#split()
fruit ="mango orange banana"
print(fruit.split()) #split the string and returns it as a list

#rsplit()
text = "one,two,three,four,five,six,seven,eigth,nine,ten"
print(text.rsplit(",", 4)) #this splits the variable named text into four parts of a list from the right at the comma sign

#splitlines()
lines = "Line 1 \nLine 2 \nLine 3"
print(lines.splitlines()) #splits the string into list at the newlines escape sequences (\n)

#join()
word = ["I", "love", "Python", "it is so fun", "fun"]
print(" ".join(word)) #joins a list of string into one string with a specified separator (in this case, whitespace)

#center()
text = "Python"
print(text.center(10, "-")) #this adds multiples of the specified character (-) to "python" until occupies 10 character space. with emphasis on "python being centralized"

#ljust()
text = "Python"
print(text.ljust(10, "*")) #this aligns the string to the left with specified width and padding with spaces or characters (in this case *)

#rjust()
text = "Python"
print(text.rjust(100, "*")) #does the same thing as ljust but to the right

#zfill()
num = "41"
print(num.zfill(5)) #pads a numeric strin on the left with zeros until it reaches a give length, in this case, it adds three 0s infront of 41 so it becomes 0041

#isalpha()
print("Lagos".isalpha()) #Ch
print("Lagos1325".isalpha()) #checks if the string contains only letter, it returns True or False

#isdigit()
print("1234".isdigit())
print("123ad".isdigit())

#isalnum
print("Python3".isalnum())
print("Python 3".isalnum()) #Checks if the string contains only letter and digits. Returns false if characters like whitespaces exist