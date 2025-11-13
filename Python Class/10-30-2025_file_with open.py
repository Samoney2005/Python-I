with open("hello_kitty.txt","r") as content:
    data = content.read()
    print(data)

'''
content =  open("hello_kitty.txt","r")

data = content.read()

print(data)

print("------------------------------------------------")

print("it adds lines to th e files")

#Append data to the file

content =  open("hello_kitty.txt","a")

#We write into the file
content.write("I live in Desoto,Texas \n")
content.write("My college is in Norman,Oklahoma \n")
content.write("The weather is cold and chilly \n")
content.write("I love Oklahoma \n")


print("-----------------------------------------")

content =  open("hello_kitty.txt","r")

data = content.read()

print(data)


#close the file
content.close()
'''


