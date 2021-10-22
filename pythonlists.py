#pythonlists
thislist  = ["apple","banana","cherry"]
print(thislist)
#lists allow duplicate values
thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)
#to print the number of items in ths list we use len() function
thislist = ["apple","banana","cherry"]
print(len(thislist))
list1 = ["apple","banana","cherry"]
list2 = [1,5,7,9,3]
list3 = [True,False,False]
#a list can contain diferent data types
list1 = ["abc",34,True,40,"male"]
#data type of the list is list
mylist = ["apple","banana","cherry"]
print(type(mylist))
#we can create a new list by using list() constructor
thislist = list(("apple","banana","cherry"))
print(thislist)
#to print the second item of the list
thislist = ["apple","banana","cherry"]
print(thislist[1])
#negetive indexing
#from the last
thislist = ["apple","banana","cherry"]
print(thislist[-1])
#return the third,fourth and fifth
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])
#to return the items from the beginning to,but NOT including,"kiwi"
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])
#return the items from "cherry" to the end
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])
#range of negetive indexing
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[-4:-1])
#check if apple is present in the list
thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes,'apple' is in the fruits list" )
#chaning list items
#change the second item
thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)
#change the second value by replacing it with two new values:
thislist = ["apple","banana","cherry"]
thislist[1:2] = ["blackcurrant","watermelon"]
print(thislist)
#change the second and third value by replacing it with one value
thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#insert watermelon as the third item
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)
#to add an item at the end of a list we use append()
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
#to append elements from another list to the current list,use the extend() method
thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)
#we can add any iterable objects like tuples,sets,dictionariesets using extend() method
#add elements of a tuple to a list
thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)
#removing elements froma a list
#remove "banana"
thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)
#removing specified index using pop()
#remove the second item
thislis = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
#remove the last item
thislis = ["apple","banana","cherry"]
thislist.pop()
print(thislist)
#the del keyword also removes the specified index
thislis = ["apple","cherry","banana"]
del thislis[0]
print(thislist)
#delete the entire list
thislist = ["apple","banana","cherry"]
del thislist
#clear the list content
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)
#printing all the items in a list one by one
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)
    #print all the items by refering to thier index number
    thislist = ["apple","banana","cherry"]
    for i in range(len(thislist)):
        print(thislist[i])
    #print all items using a while loop to go through all the index numbers
    thislis = ["apple","banana","cherry"]
    i = 0
    while i< len(thislist) :
        print(thislist[i])
        i = i+1
    #a short hand for loop that will print all items in a list
    thislist = ["apple","banana","cherry"]
    [print(x) for x in thislist]
    #list comprehension
    fruits = ["apple","banana","cherry","kiwi","mango"]
    newlist = []
    for x in fruits:
        if "a" in x:
            newlist.append(x)
            print(newlist)
#list comprehension the code becomes easier
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#only accept items that are not apple
newlist = [x for x in fruits if x != "apple" ]
print(newlist)
#with no if statement
newlist = [x for x in fruits]
#we can use the range() function to create an iterable
newlist = [x for x in range(10)]
#accpet only numbers less than five
newlist = [x for x in range(10) if x < 5]
#set the values in the newlist to uppercase
newlist = [x.upper() for x in fruits]
#set all the values in the list to helo
newlist = ["hello" for x in fruits]
#return orange instead of banana
newlist = [x if x != "banana" else "orange" for x in fruits]
#sort the list alphabetically
thislist = ["orange" ,"mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)
#sort this list numerically
thislist = [100,50,65,82,23]
thislist.sort()
print(thislist)
#sort the list descending
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse =True)
print(thislist)
#sort the list descending
thislist  = ["orange", "mango" ,"kiwi","pineapple","banana"]
thislist.sort(reverse = True)
print(thislist)
#sort the list descending
thislist = [100,50,65,82,23]
thislist.sort(reverse = True)
print(thislist)
#sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n-50)
    thislist = [100,50,65,82,23]
    thislist.sort(key = myfunc)
    print(thislist)
#case insensitive sort
thislist = ["banana","orange","kiwi","cherry"]
thislist.sort()
print(thislist)
#perform a case-insensitive sort of the list
thislist = ["banana","orange","kiwi","cherry"]
thislist.sort(key = str.lower)
print(thislist)
#reverse() method
thislist = ["banana","orange","kiwi","cherry"]
thislist.reverse()
print(thislist)
#make a copy of a list with the copy() method
thislist = ["apple", "banana","cherry"]
mylist = thislist.copy()
print(mylist)
#make a copy of alist with the list() method
thislist = ["apple","banana","cherry"]
mylist  = list(thislist)
print(mylist)
#join two list
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1+list2
print(list3)
#append list2 into list1
list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)
    print(list1)
#using extend()
list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)