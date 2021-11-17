#if statement
a = 33
b = 200
if b>a:
    print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
     print("b is greater than a")
elif a == b:
    print("a and b are equal")
#else
a = 200
b = 33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
#we can also have else without the elif
a = 200
b = 33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#one line if statement
if a >b:
    print("a is greater than b")

#one line if ele statement
a = 2
b = 330
print("A") if a>b else print("B")
#one line if else stement,with 3 conditions
a = 330
b = 330
print("A") if a>b else print("=") if a == b else print("B")
#test if a is greater than b,AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c >a:
    print("Both conditions are true")
#test if a is greater than b,OR if a is gre
a = 200
b = 33
c = 500
if a>b or a>c:
    print("At least one of the conditions is true")
#nested if statement
x = 41
if x>10:
    print("aboce ten")
    if x>20:
        print("and also above 20")
    else :
            print("but not above 20")
#the pass statement
a = 33
b = 200
if b>a:
    pass
