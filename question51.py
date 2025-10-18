def divide():
    return 5 / 0

try:
    divide()
except ZeroDivisionError:
    print("You can't divide by zero!")
except:
    print("Any other exception")
