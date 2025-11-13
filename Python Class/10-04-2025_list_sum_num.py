list=[1,2,3,4,5]


# Function Declaration
def add():
    list=[1,2,3,4,5]
    sum = 0
    for x in list:
        sum = sum + x
    return(sum)


result = add()


print(f"The result is: {result}")
