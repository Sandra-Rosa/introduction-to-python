thisdict = {"brand": "Ford",
"model":"Mustang",
"year": 1964}
#create and print a dictionary
thisdict = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1964
}
print(thisdict["brand"])
#duplicate values will overwrite existing values
thisdict = {
    "brand": "ford",
    "model":"mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
#print the number of items in the dictionary
print(len(thisdict))
#string,int,boolean and list data types
thisdict = {
    "brand": "ford",
    "electric": False,
    "year": 1964,
    "colors": ["red","white","blue"]
}
#print the data type of dictionary
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
print(type(thisdict))
#get the value of the "model" key
thisdict  = {
    "brand":"ford",
    "model": "mustang",
    "year": 1964
}
x = thisdict["model"]
#get the value of the "model" key
x = thisdict.get("model")
#get a list of the keys
x = thisdict.keys()
#add a new item to the original dictionary and see that the keys list gets updated as well
car = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
x = cars.keys()
print(x)
car["color"] = "white"
print(x)
#get a list of the values:
x = thisdict.values()
#get a list of the key:value pairs
x = thisdict.items()
#make a change in the original dictionary and see that the items list gets updated as well
car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)
#add a new item to the original dictionary and see that the items list gets updated as weel
car = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)
#check if "model" is present in the dictionary
thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes,'model' is one of the keys in thisdict dictionary")
#change the year to 2018
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
thisdict["year"] = 2018
#update the "year" of the car by using the update() method
thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
#adding items
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#add a color item to the dictionary by using the update() method
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
#the pop() method removes the item with the specified key name
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)
#the popitem() method removes the last inserted item
thisidict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)
#the del keyword removes the item with specified key name
thisidct = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
#THE DEL KEYWORD CAN ALSO DELETE THE DICTIONARY COMPLETELY
thsidict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
del thisidict
print(thisidct)
#the clear() method empties the dictionary
thsidict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
thisdict.clear()
print(thisidct)
#print all key names in the dictionary one by one
for x in thisdict:
    print(x)
#print all values in the dictionary,one by one
for x in thisdict:
    print(thisdict[x])
#you can also use the values() method to return values of a dictionary
for x in thisidct.values():
    print(x)
#you can use the keys() method to return the keys of a dictionary
for x in thisidct.keys():
 print(x)
#loop through both keys and values,by using the items() method
for x,y in thisdict.items():
    print(x,y)
#make a copy of a dictionary with the copy() method
thisdict = {
    "brand":"ford",
    "model": "mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#make a copy of a dictionary with the dict() function
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
mydict = dict(thisidict)
print(mydict)
#create a dictionary that contain three dictionaries
myfamily = {
    "child1": {
        "name": "emil",
        "year": 2004
    },
    "child2" : {
        "name": "tobias",
        "year":2007
    },
    "child3": {
        "name" : "linus",
        "year":2011
    }
}
#create three dictionaries,then create one dictioanry that will conatain the other three dictionaries
child1 = {
    "name":"emil",
    "year": 2004
}
child2 = {
    "name":"tobias",
    "year": 2007
}
child3 = {
    "name":"linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
