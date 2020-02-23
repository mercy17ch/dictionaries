'''program to show dictionaries'''
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values
#
#creating dictionary#
thisdict={"name":"mercy",
           "sex":"female",
           "age":23}
print(thisdict)

#dictionary methods#
#clear()	Removes all the elements from the dictionary#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
person.clear()
print(person)
#copy()	Returns a copy of the dictionary#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
x=person.copy()

print(x)
#fromkeys() Returns a dictionary with the specified keys and value#
x = ('key1', 'key2', 'key3')
y = 4

thisdict = dict.fromkeys(x, y)

print(thisdict)
#get()	Returns the value of the specified key#

person = {"name":"mercy",
           "sex":"female",
           "age":23}
x=person.get("age")
print(x)
#items()	Returns a list containing a tuple for each key value pair#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
x=person.items()
print(x)
#keys()	Returns a list containing the dictionary's keys#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
x=person.keys()
print(x)
#pop()	Removes the element with the specified key#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
person.pop("age")
print(person)
#popitem()	Removes the last inserted key-value pair#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
person.popitem()
print(person)
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value#

person = {"name":"mercy",
           "sex":"female",
           "age":23}
x=person.setdefault("age","18")
print(x)
#update()	Updates the dictionary with the specified key-value pairs#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
person.update({"skin color":"brown"})
print(person)
#values()	Returns a list of all the values in the dictionary#
person = {"name":"mercy",
           "sex":"female",
           "age":23}
x=person.values()
print(x)






