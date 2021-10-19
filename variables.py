x = 5
y = "John"
print(x)
print(y)

x = 4
x = "sally"
print(x)

#casting
x = str(3)
y = int(3)
z = float(3)

#get the type
x = 5
y = "John"
print(type(x))
print(type(y))

#single or double qoutes
"""
string variables can be declared either by using
single or double qoutes:
"""
x = "JOhn"
#is same as
x = 'John'

#case sensitive
"""
variable names are case sensitive
"""
a = 4
A = "sally"
#A willnot overwrite a

#variable name
"""
must start with a letter or the underscore
cannot start with a number.
can only contain (A-z,0-9 and _)
case sensitive
"""

#Multi word variable names

"""
camel case:myVariableName
Pascal case:MyVariableName
Snake case:my_variable_name
"""

#Many values to Multiple Variables
x, y, z  = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Output variables
x = "awesome"
print("Python is " + x)

x = "python is "
y = "awesome"
z = x+y
print(z)

x = 5
y = 10
print(x+y)

#global variables
x = "awesome"

def myfunc():
    print("Python is " + x)
    myfunc()

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
#the global keyword
def myfunc():
    global x
    x = "fantastic"

    myfunc()
    print("Python is " + x)    

x = "awesomw"

def myfunc():
    global x
    x = "fantastic"

    myfunc()

    print("Python is " + x)