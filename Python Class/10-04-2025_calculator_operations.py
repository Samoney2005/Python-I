num_1 = int(input("Enter your first number:"))
num_2 = int(input("Enter your second number:"))
operations = input("What symbol do you want to use (+,-,*,/)?")

#fonction declaration

def add(a,b):


    return(a+b)


def sub(a,b):


    return(a-b)

def multi(a,b):


    return(a*b)

def divi(a,b):

    return(a/b)

symbols = {"+":add,"-":sub,"*":multi,"/":divi,}
print(symbols)
print(symbols["+"](4,5))
print(symbols[operations])

#fonction call


#summm =  
summm = add(num_1, num_2)


symbols[operations] =  add, sub, multi, divi

print("The value of the operation is: ")

#symb = symbols[operations]

#print(symb(num_1, num_2))


print(f"The result is {summm}")


'''
list=[a,b,c,d,e]
def add(a,b):
 for in list:

    return(a+b)
'''
