number = input("Insert number: ")
try:
    if (int(number) < 20):
        print("Less than 20: {}".format(number))
    elif (int(number) > 19 and int(number)<40):
        print("Between 20 and 39: {}".format(number))
    elif (int(number) > 39 and int(number) < 60):
        print("Between 40 and 59: {}".format(number))
    else:
        print("More than 60: {}".format(number))
except Exception as e:
    print(e)