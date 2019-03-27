operations = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "*": lambda x, y: x * y,
              "/": lambda x, y: x / y,
              "e": lambda x, y: x ** y,
              }

try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    x = input("Operation (+,-,*,/,e): ")
    print(operations[x](a, b)) if (x in operations.keys()) else print("Invalid operator.")
except Exception as e:
    print(e)

# Test
assert 5+4 == operations["+"](5, 4)
assert 5-4 == operations["-"](5, 4)
assert 5*4 == operations["*"](5, 4)
assert 5/4 == operations["/"](5, 4)
assert 5**4 == operations["e"](5, 4)
