#Python Numbers
"""
int
float
complex
"""

x = 1 #int
y = 2.8 #float
z = 1j #complex

#int
x = 1
y =1029840984084
z = -988374873

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#example 2 on float
x = 35e3
y = 12E4
z = -87.7e100

#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#type conversion
x = 1 #int
y = 2.8 #float
z = 1j #complex
#convert from int to float
a = float(x)
#convrt from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number
import random
print(random.randrange(1,10))