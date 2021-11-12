#create a tuple
thistuple = ("apple","banana","cherry")
print(thistuple)
#tuples allow duplicate values
thistuple = ("apple","banana","cherry")
print(thistuple)
# print the number of items in the tuple
thistuple = ("apple","banana","cherry")
print(len(thistuple))
#one item tuple,remember the comma
thistuple = ("apple",)
print(type(thistuple))
#not a tuple
thistuple = ("apple")
print(type(thistuple))
#tuple items can be of any data types
tuple1 = ("apple","banana","cherry")
tuple2 = (1,5,7,9,13)
tuple3 = (True,False,False)
#a tuple with strings,integers and boolean values
tuple1 = ("abc",34,True,40,"male")
#what is the data type of a tuple?
mytuple = ("appple","banana","cherry")
print(type(mytuple))
#using the tuple method to make a tuple
thistuple = (("apple","banana","cherry"))
print(thistuple)
#print the second item in the tuple
thistuple = ("apple","banana","cherry")
print(thistuple[1])
#print the last item of the tuple with negetive indexing
thistuple = ("apple","banana","cherry")
print(thistuple[-1])
#with range of indexes
#return the third,fourth and fifth item
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])
#this example returns the items from the beginning to,but NOT included "kiwi"
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[:4])
#this example returns the items from cherry and to the end
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:])
#this example returns the items from index -4(included) to inex -1(excluded)
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[-4:-1])
#check if apple is present in the tuple
thistuple = ("apple","banana","cherry")
if "apple" in thistuple:
    print("yes,apple is in thistuple")
#convert the tuple into a list to be able to change it
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#convert the tuple into a list,add "orange",and convert it back into a tuple
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#create a new tuple with th e value "orange", and add that tupleth
thistuple = ("apple","banana","cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#convert the tuple into a list,remove "apple",and convert it back into a tuple
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#or you can delete the tuple completely
#the del keyword can delete the tuple completely
thistuple = ("apple","banana","cherry")
del thistuple
print(thistuple)
#packing a tuple
fruits = ("apple","banana","cherry")
#unpacking a tuple
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)
#assign the rest of the values as a lit called "red"
fruits = ("apple","banana","cherry","strawberry","respberry")
(green,yellow,*red) = fruits
print(green)
print("yellow")
print("red")
#add a list of values the "tropic" variablr
fruits = ("apple","mango","pappaya","pineapple","cherry")
(green,*tropic,red) = fruits
print(green)
print(tropic)
print(red)
#iterate through the items and print the values
thsituple  = ("apple","banana","cherry")
for x in thistuple:
    print(x)
#print al items by refering to thier index numbers
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
#join two tuples
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 =tuple1+tuple2
print(tuple3)
#multiply the fruits tuple by 2
fruits = ("apple","banana","cherry")
mytuple = fruits*2
print(mytuple)
