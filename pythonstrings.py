#strings
print("hello")
print('hello')
#assign string to a variable
a = "hello"
print(a)

#multiline strings
#we can use three double qoutes
a = """lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#or three single qoutes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#get the character at position 1
a = "hello world!"
print(a[1])

#loop through the letters in the word "banana":
for x in "banana":
    print(x)
#to find the length of the string
a = "Hello world!"
print(len(a))

#check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#use it in a if statement
txt = "the best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#check if "expensive" is NOT present in the following text:
txt = "The best things in the life are free!"
print("expensive" not in txt)
#use it in a if statement
txt = "The best things in the life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# python-slicing strings
#get the characters from position 2 to position 5(not included)
b = "Hello world!"
print(b[2:5])
#note:The first character has index 0.

#get the characters from the start to postition 5(not included)
b = "Hello world"
print(b[:5])

#get the characters from position 2,and all the way to the end:
b = "Hello world!"
print(b[2:])

"""Get the characters:
From: "o" in "World! (position-5)
To,but not included: "d" in "World!(position-2)"""
b = "hello, World!"
print(b[-5:-2])

#modify strings
#upper case
a = "Hello world!"
print(a.upper())

#lower case
a = "Helllo World!"
print(a.lower())

#remove whitespace
a = " Hello, World!"
print(a.strip())

#replace string
a = "Hello,World!"
print(a.replace("H", "J"))

#split string
a = "Hello World!"
print(a.split(","))

#string concatenation
#merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a+b
print(c)

#to add a space between them, add a " ":
a = "Hello"
b = "World"
c = a+" "+b
print(c)

#format strings
#we cannot combine strings and numbers using +
#we use format() instead
#use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#the format() method takes unlimited number of arguments, and are placed into the respective place holders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

#you can use index numbera {0} to be sure the aguments are placed in the correct place holers:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))

#escape characters
txt = "We are so-called \"Vikings\"from the north."
print(txt)