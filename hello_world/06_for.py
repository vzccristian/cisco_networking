myList = ["Cristian", "Ana", "Fran", "Hulio", "Stallman"]
selected = []
for x in myList:
    print(x)
    if x.__contains__("a"):
        selected.append(x)

print(selected)
