# Introduction to python

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

## Python Operators
Operators are used to perform operations on variables and values.

### Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

### Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator |	Name |	Example	|
|----------|-------|----------|
| + |	Addition |	x + y	|
| - |	Subtraction |	x - y	|
| * |	Multiplication |	x * y |	
| / |	Division |	x / y	|
| % |	Modulus |	x % y	|
| ** |	Exponentiation |	x ** y |	
| // |	Floor division |	x // y	|

### Python Assignment Operators
Assignment operators are used to assign values to variables:

| Operator |	Example |	Same As |	
|----------|-----------|--------|
| = |	x = 5 |	x = 5	|
| += |	x += 3 |	x = x + 3	|
| -= |	x -= 3 |	x = x - 3	|
| *= |	x *= 3 |	x = x * 3	|
| /= |	x /= 3 |	x = x / 3	|
| %= |	x %= 3 |	x = x % 3	|
| //= | x //= 3 |	x = x // 3 |	
| **= |	x **= 3 |	x = x ** 3	|
| &= |	x &= 3 |	x = x & 3	 |
| l= |	x l= 3 |	x = x l 3	|
| ^= |	x ^= 3 |	x = x ^ 3	 |
| >>= |	x >>= 3 |	x = x >> 3	|
| <<= |	x <<= 3 |	x = x << 3	

### Python Comparison Operators
Comparison operators are used to compare two values:

| Operator |	Name |	Example |
|----------|--------|---------|
| == |	Equal |	x == y	|
| != |	Not equal |	x != y	|
| > |	Greater than |	x > y	|
| < |	Less than |	x < y	|
| >= |	Greater than or equal to |	x >= y	|
| <= |	Less than or equal to |	x <= y |

### Python Logical Operators
Logical operators are used to combine conditional statements:

| Operator |	Description |	Example |	
|----------|--------------|---------|
| and | 	Returns True if both statements are true |	x < 5 and  x < 10	|
| or |	Returns True if one of the statements is true |	x < 5 or x < 4 |	
| not |	Reverse the result, returns False if the result is true| not(x < 5 and x < 10) |

### Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator |	Description |	Example |
|----------|--------------|---------|
| is | 	Returns True if both variables are the same object |	x is y	|
| is not |	Returns True if both variables are not the same object |	x is not y |

### Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

| Operator |	Description |	Example	|
|----------|--------------|---------|
| in |	Returns True if a sequence with the specified value is present in the object	| x in y	|
| not in |	Returns True if a sequence with the specified value is not present in the object |	x not in y	|

### Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

| Operator 	Name |	Description |
|-----------------|--------------|
| & | 	AND |	Sets each bit to 1 if both bits are 1 |
| l |	OR |	Sets each bit to 1 if one of two bits is 1 |
| ^	 |XOR |	Sets each bit to 1 if only one of two bits is 1 |
| ~ | 	NOT	| Inverts all the bits |
| << |	Zero fill left shift |	Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| >> |	Signed right shift |	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

### List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
### List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

### Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
### Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

### Allow Duplicates
Since lists are indexed, lists can have items with the same value
### List Length
To determine how many items a list has, use the len() function
### List Items - Data Types
List items can be of any data type
### type()
From Python's perspective, lists are defined as objects with the data type 'list'
### The list() Constructor
It is also possible to use the list() constructor when creating a new list.
### Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered* and changeable. No duplicate members.
### Change Item Value
To change the value of a specific item, refer to the index number
### Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
### Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index
### Append Items
To add an item to the end of the list, use the append() method
### Extend List
To append elements from another list to the current list, use the extend() method.
### Remove Specified Item
The remove() method removes the specified item.
### Remove Specified Index
The pop() method removes the specified index.

The del keyword also removes the specified index

The del keyword can also delete the list completely.

### Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

### Loop Through a List
You can loop through the list items by using a for loop
### Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
### Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

Remember to increase the index by 1 after each iteration.
### Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:
### List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#### The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

##### Condition
The condition is like a filter that only accepts the items that valuate to True.
#### Iterable
The iterable can be any iterable object, like a list, tuple, set etc.
##### Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
### Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default
### Sort Descending
To sort descending, use the keyword argument reverse = True
### Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first)
### Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
### Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.
### Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy()
Another way to make a copy is to use the built-in method list().
### Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.
## List Methods
Python has a set of built-in methods that you can use on lists.

|Method |	Description |
|-------|-------------|
| append() |	Adds an element at the end of the list |
| clear() |	Removes all the elements from the list |
| copy() |	Returns a copy of the list |
| count() |	Returns the number of elements with the specified value |
| extend() |	Add the elements of a list (or any iterable), to the end of the current list |
| index() |	Returns the index of the first element with the specified value |
| insert() |	Adds an element at the specified position |
| pop() |	Removes the element at the specified position |
| remove() |	Removes the item with the specified value |
| reverse() |	Reverses the order of the list |
| sort() |	Sorts the list |
## Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
### Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

### Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

### Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

### Allow Duplicates
Since tuples are indexed, they can have items with the same value
### Tuple Length
To determine how many items a tuple has, use the len() function
### Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
### Tuple Items - Data Types
Tuple items can be of any data type
### type()
From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>
### The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
### Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets
### Negative Indexing
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.
### Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

### Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple
### Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword
### Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
### Add Items
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
2.Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple
### Remove Items
Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
### Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple
### Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
### Loop Through a Tuple
You can loop through the tuple items by using a for loop
### Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
### Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

Remember to increase the index by 1 after each iteration.
### Join Two Tuples
To join two or more tuples you can use the + operator
### Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator
### Tuple Methods
Python has two built-in methods that you can use on tuples.

| Method |	Description |
|--------|--------------|
| count() |	Returns the number of times a specified value occurs in a tuple |
| index() |	Searches the tuple for a specified value and returns the position of where it was found |

## Sets
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

Sets are written with curly brackets.
### Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

### Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

### Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

### Duplicates Not Allowed
Sets cannot have two items with the same value.
### Get the Length of a Set
To determine how many items a set has, use the len() method.
### Set Items - Data Types
Set items can be of any data type
### type()
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>
### The set() Constructor
It is also possible to use the set() constructor to make a set.
### Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
## Python - Access Set Items
### Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
### Change Items
Once a set is created, you cannot change its items, but you can add new items
### Add Set Items
To add one item to a set use the add() method.
### Add Sets
To add items from another set into the current set, use the update() method.
### Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
### Remove Item
To remove an item in a set, use the remove(), or the discard() method.

You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.
### Loop Items
You can loop through the set items by using a for loop
### Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another
### Keep ONLY the Duplicates
The intersection_update() method will keep only the items that are present in both sets.

The intersection() method will return a new set, that only contains the items that are present in both sets.
### Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
### Set Methods
Python has a set of built-in methods that you can use on sets.

| Method |	Description |
|--------|--------------|
| add() |	Adds an element to the set |
| clear() |	Removes all the elements from the set |
| copy() |	Returns a copy of the set |
| difference() |	Returns a set containing the difference between two or more sets |
| difference_update() |	Removes the items in this set that are also included in another, specified set |
| discard() |	Remove the specified item |
| intersection() |	Returns a set, that is the intersection of two other sets |
| intersection_update() |	Removes the items in this set that are not present in other, specified set(s) |
| isdisjoint() |	Returns whether two sets have a intersection or not |
| issubset() |	Returns whether another set contains this set or not |
| issuperset() |	Returns whether this set contains another set or not |
| pop() |	Removes an element from the set |
| remove() |	Removes the specified element |
| symmetric_difference() |	Returns a set with the symmetric differences of two sets |
| symmetric_difference_update() |	inserts the symmetric differences from this set and another |
| union() |	Return a set containing the union of sets |
| update() |	Update the set with the union of this set and others |

## Python Dictionaries
### Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
### Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
### Ordered or Unordered?
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
### Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

### Duplicates Not Allowed
Dictionaries cannot have two items with the same key
### Dictionary Length
To determine how many items a dictionary has, use the len() function
### Dictionary Items - Data Types
The values in dictionary items can be of any data type
### type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
### Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
### Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets

There is also a method called get() that will give you the same result
### Get Keys
The keys() method will return a list of all the keys in the dictionary.

The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
### Get Values
The values() method will return a list of all the values in the dictionary.

The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

### Get Items
The items() method will return each item in a dictionary, as tuples in a list.

The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
### Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword
### Change Values
You can change the value of a specific item by referring to its key name
### Update Dictionary
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
### Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it
### Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs
### Removing Items
There are several methods to remove items from a dictionary
### Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
### Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Another way to make a copy is to use the built-in function dict().
### Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
### Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

| Method |	Description |
|--------|--------------|
| clear() |	Removes all the elements from the dictionary |
| copy() |	Returns a copy of the dictionary |
| fromkeys() |	Returns a dictionary with the specified keys and value |
| get() |	Returns the value of the specified key |
| items() |	Returns a list containing a tuple for each key value pair |
| keys() |	Returns a list containing the dictionary's keys |
| pop() |	Removes the element with the specified key |
| popitem() |	Removes the last inserted key-value pair |
| setdefault() |	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update() |	Updates the dictionary with the specified key-value pairs |
| values() |	Returns a list of all the values in the dictionary |

### Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

### Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

### Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
### Else
The else keyword catches anything which isn't caught by the preceding conditions.
### Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement
### Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
This technique is known as Ternary Operators, or Conditional Expressions.
### And
The and keyword is a logical operator, and is used to combine conditional statements
### Or
The or keyword is a logical operator, and is used to combine conditional statements
### Nested If
You can have if statements inside if statements, this is called nested if statements.
### The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
### Python Loops
Python has two primitive loop commands:

-while loops
-for loops
### The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

### The break Statement
With the break statement we can stop the loop even if the while condition is true

### The continue Statement
With the continue statement we can stop the current iteration, and continue with the next
### The else Statement
With the else statement we can run a block of code once when the condition no longer is true
## Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

The for loop does not require an indexing variable to set beforehand.

### Looping Through a String
Even strings are iterable objects, they contain a sequence of characters
### The break Statement
With the break statement we can stop the loop before it has looped through all the items
### The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next
### The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
### Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished
### Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"
### The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

## Python Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
### Creating a Function
In Python a function is defined using the def keyword
### Calling a Function
To call a function, use the function name followed by parenthesis
### Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name
### Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.
### Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
### Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
### Keyword Arguments
You can also send arguments with the key = value syntax.
### Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly
### Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value
### Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
### Return Values
To let a function return a value, use the return statement.
### The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
### Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.


## Python Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Lambda functions can take any number of arguments

### Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
