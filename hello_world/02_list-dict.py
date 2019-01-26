import random

myList1 = ["esto", "es", "una", "lista", "para", "cisco"]
myList2 = [x for x in range(1, 10)]
myList3 = myList1 + myList2 + [random.random() for x in range(1, 10)]

print(myList1)
print(myList2)
print(myList3)

lastMyList1 = myList1[-1]
lastMyList2 = myList2[-1]
lastMyList3 = myList3[-1]

print("Last value of first list: {}".format(lastMyList1))
print("Last value of second list: {}".format(lastMyList2))
print("Last value of third list: {:.2f}".format(lastMyList3))

myDict = {"Cristian":"Curso Cisco", "Juan":"Buen libro"}

print(myDict)
print(myDict.keys())
print(myDict.values())