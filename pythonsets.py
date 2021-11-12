myset = {"apple","banana","cherry"}
thisset = {"apple","banana","cherry"}
print(thisset)
#duplicate values will be ignored
thisset = {"apple","banana","cherry","apple"}
print(thisset)
#get the number of items in a set
thisset = {"apple","banana","cherry"}
print(len(thisset))
#set items can be of any data types
set1 = {"apple","banana","cherry"}
set2 = {1,5,7,9,3}
set3 = {True,False,False}
#a set can contain different data types
set1 = {"abc",34,True,40,"male"}
#what is the datat type of a set
myset = {"apple","banana","cherry"}
print(type(myset))
#using the set() constructor to make a set
thisset = set(("apple","banana","cherry"))
print(thisset)
#loop through the set,and print the values
thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)
#check if "banana" is present in the set
thisset = {"apple","banana","cherry"}
print("banana" in thisset)
#add an item to a set using the add() method
thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)
#add items from tropical into thisset
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
#add elements of a list to at set
thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]
thisset.update(mylist)
print(thisset)
#remove "banana" by using the remove() method
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)
#remove "banana" by using the discard() method
thisset = {"apple","banana","cherry"}
thisset.dicard("banana")
print(thisset)
#remove the last item by using the pop() method
thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(x)
print(thissset)
#the clear method empties the set
thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)
#the del keyword will delete the set completely
thisset = {"apple","banana","cherry"}
del thisset
print(thisset)
#loop through the set,and print the values
thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)
#the union() method returns a new set with all items from both sets
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)
#the update() method inserts the items in set2 into set1
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)
#keep the items that exist in both set x and set y
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.intersection_update(y)
print(x)
#return a set that contains the items that exist in both set x,set y
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z=x.intersection(y)
print(z)
#keep the items that are not present in both sets
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.symmetric.difference_update(y)
print(x)
#return a set that contains all items from both sets,except items that are present in both
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z = x.symmetric_difference(y)
print(z)