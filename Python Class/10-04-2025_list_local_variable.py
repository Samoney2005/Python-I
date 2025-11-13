#car=[1,2,3,4,5]


# Function Declaration
def add():
    car=[1,2,3,4,5]
    sum = 0
    print(car)
    for x in car:
        sum = sum + x
    return(sum)


result = add()


print(f"The result is: {result}")

#print(car)
