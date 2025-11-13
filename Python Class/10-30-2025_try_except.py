try:

    number = int(input("type a number : "))
    result = 100/number

except ZeroDivisionError:
    print("You can't division by zero")

else:
    print(result)
