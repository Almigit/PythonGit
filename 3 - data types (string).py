# Strings

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

#You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1]) # result e




"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""

sentence = "Heldlo world"
twoLetters = ""
counter = 0

for letter in sentence:
    if (counter % 2 != 0):
        twoLetters = twoLetters + letter
        print(twoLetters)
        twoLetters = ""
    else:
        twoLetters = twoLetters + letter
    counter = counter + 1
    if(len(sentence) % 2 != 0):
        if(counter == len(sentence)):
            print(letter)

sentence2 = "Big red dog"

print(sentence2) #full
print(sentence2[0]) #B
print(sentence2[3]) #space
print(len(sentence2)) #10
print(sentence2[len(sentence2) - 1]) #g

name = "Alexys"
name2 = "Alexy"
name3 = "Alex"
name4= "Al"
threeLetters = ""
counter2 = 1

for letter in name4:
    if(counter2 % 3 == 0): # если делится на три тогда мы выдаем текст и обновляем наш буфер
        threeLetters = threeLetters + letter
        print(threeLetters)
        threeLetters = ""
    else:
        threeLetters = threeLetters + letter # пока не делится не 3 мы прибалвяем буквы

    if(len(name4) % 3 != 0):
       if(counter2 == len(name4)):
           print(threeLetters)

    counter2 = counter2 + 1






