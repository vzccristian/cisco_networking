operations = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "*": lambda x, y: x * y,
              "/": lambda x, y: x / y,
              "e": lambda x, y: x ** y,
              }

def calculator(a, b, x):
    try:
        return (operations[x](a, b)) if (x in operations.keys() or x in len(list(operations.keys()))) else print(
            "Invalid operator.")
    except TypeError as e:
        x = int(x)
        if x > -1 and x < len(list(operations.keys())):
            return (operations[list(operations.keys())[x]](a, b))
        else:
            return ("Invalid operator.")
    except Exception as e:
        return ("Invalid operator.")

# Test
assert 5 + 4 == calculator(5, 4, "+")
assert 5 - 4 == calculator(5, 4, "-")
assert 5 * 4 == calculator(5, 4, "*")
assert 5 / 4 == calculator(5, 4, "/")
assert 5 ** 4 == calculator(5, 4, "e")

assert 5 + 4 == calculator(5, 4, 0)
assert 5 - 4 == calculator(5, 4, 1)
assert 5 * 4 == calculator(5, 4, 2)
assert 5 / 4 == calculator(5, 4, 3)
assert 5 ** 4 == calculator(5, 4, 4)


# Main
if __name__ == '__main__':
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        x = input("Operation (+,-,*,/,e): ")
        print(calculator(a, b, x))
    except Exception as e:
        print(e)
