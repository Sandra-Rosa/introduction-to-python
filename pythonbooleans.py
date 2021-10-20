#Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10<9)

a = 200
b = 33

if b > a :
    print("b is grater than a")

else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

#evalute two variables
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#most values are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#function
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

#functions can return a boolean value
def myFunction() :
    return True
print(myFunction())

def myFunction():
    return True
if myFunction():
    print("Yes!")
else:
    print("No!")

x = 200
print(isinstance(x,int))

