try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    x = input("Operation (+,*,/,e): ")

    if x == "+": print(a+b)
    elif x == "*": print(a*b)
    elif x == "/": print(a/b)
    elif x == "e": print(a**b)
    else: print("Invalid operator.")
except Exception as e:
    print(e)