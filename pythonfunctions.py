def my_function():
    print("Hello from a function")
#calling a function
def my_function():
    print("Hello from a function")
my_function()
#arguments
def my_function(fname):
    print(fname + "Refsnes")
my_function("emil")
my_function("tobias")
my_function("Linus")
#this function expects 2 arguments,and gets 2 arguments
def my_function(fname,lname):
   print(fname + " " + lname)

my_function("Emil","Refsnes")
#if the number of arguments is unknown,add a * before the parameter name
def my_function(*kids) :
    print("The youngest child is " + kids[2])
my_function("Emil","Tobias","Linus")
#keyword arguments
def my_function(child3,child2,child1):      
       print("The youngest child is "+ child3)

my_function(child1 = "Emil",child2 = "Tobias",child3 = "Linus")
#if the number of keyword arguments is unknown,add a double  ** before the parameter name
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#default parameter value
def my_function(country ="Norway"):
    print("Iam from" +country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]

my_function(fruits)
#return values
def my_function(x):
    return 5* x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#the pass statement
def my_function():
    pass
#recursion example
def tri_recursion(k):
    if(k>0):
        result = k+ tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion example results")
tri_recursion(6)