# introduction to python

## What is Python?

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

1.web development (server-side)

2.software development

3.mathematics

4.system scripting.

### What can Python do?
- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.


### Why Python?


- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-oriented way or a functional way.

  <p align="center">
  <img width="600px" src="https://user-images.githubusercontent.com/84260242/137849465-31641064-3b18-4817-bfbd-9f606faa366b.png"/>
  </p>

### Basic data types in python
Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

## Python casting
### Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

- int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
- float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
## Python strings

### Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
### Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
### Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

### String Length
To get the length of a string, use the len() function.

### Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.

### Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

### Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

### Slice From the Start
By leaving out the start index, the range will start at the first character

### Slice To the End
By leaving out the end index, the range will go to the end

### Negative Indexing
Use negative indexes to start the slice from the end of the string

### Modify strings
Python has a set of built-in methods that you can use on strings.
The upper() method returns the string in upper case
The lower() method returns the string in lower case
The strip() method removes any whitespace from the beginning or the end
The replace() method replaces a string with another string
The split() method splits the string into substrings if it finds instances of the separator

### String Concatenation
To concatenate, or combine, two strings you can use the + operator.

( we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are)

### Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

| CODE    | RESULT |
|  ----------- | ----------- |
|  \\'     | SINGLE QOUTE    |
|  \\\  | BACKSLASH       |
|  \\n  | NEW LINE |
|  \\r  | CARRIAGE RETURN |
|  \\t  | TAB  |
|  \\b  | BACKSPACE |
|  \\f  | FORM FEED |
|  \ooo | OCTAL VALUE |
|  \\xhh | HEX VALUE |

## STRING METHODS
|Method |	Description |
|------------|------------|
| capitalize()  |  	Converts the first character to upper case  |
|  casefold()  |	Converts string into lower case  |
|  center()  |	Returns a centered string  |
|  count()  |	Returns the number of times a specified value occurs in a string  |
|  encode()  |	Returns an encoded version of the string  |
|  endswith()  |	Returns true if the string ends with the specified value  |
|  expandtabs()  |	Sets the tab size of the string  |
|  find()  |	Searches the string for a specified value and returns the position of where it was found  |
|  format()  |	Formats specified values in a string  |
|  format_map()  |	Formats specified values in a string  |
|  index()  |	Searches the string for a specified value and returns the position of where it was found  |
|  isalnum()  |	Returns True if all characters in the string are alphanumeric  |
|  isalpha()  |	Returns True if all characters in the string are in the alphabet  |
|  isdecimal() |	Returns True if all characters in the string are decimals |
| isdigit() |	Returns True if all characters in the string are digits |
| isidentifier() |	Returns True if the string is an identifier |
| islower() |	Returns True if all characters in the string are lower case |
| isnumeric() |	Returns True if all characters in the string are numeric |
| isprintable() |	Returns True if all characters in the string are printable |
| isspace() |	Returns True if all characters in the string are whitespaces |
| istitle() |	Returns True if the string follows the rules of a title |
| isupper() |	Returns True if all characters in the string are upper case |
| join() |	Joins the elements of an iterable to the end of the string |
| ljust() |	Returns a left justified version of the string |
| lower() |	Converts a string into lower case |
| lstrip() |	Returns a left trim version of the string |
| maketrans() |	Returns a translation table to be used in translations |
| partition() |	Returns a tuple where the string is parted into three parts | 
| replace() |	Returns a string where a specified value is replaced with a specified value |
| rfind() |	Searches the string for a specified value and returns the last position of where it was found |
| rindex() |	Searches the string for a specified value and returns the last position of where it was found |
| rjust() |	Returns a right justified version of the string |
| rpartition() |	Returns a tuple where the string is parted into three parts |
| rsplit() |	Splits the string at the specified separator, and returns a list |
| rstrip() |	Returns a right trim version of the string |
| split() |	Splits the string at the specified separator, and returns a list |
| splitlines() |	Splits the string at line breaks and returns a list |
| startswith() |	Returns true if the string starts with the specified value |
| strip() |	Returns a trimmed version of the string |
| swapcase() |	Swaps cases, lower case becomes upper case and vice versa |
| title() |	Converts the first character of each word to upper case |
| translate() |	Returns a translated string |
| upper() |	Converts a string into upper case |
| zfill() |	Fills the string with a specified number of 0 values at the beginning |
### Python Booleans
Booleans represent one of two values: True or False.

### Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer

### Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return

### Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.


### Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False

One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
