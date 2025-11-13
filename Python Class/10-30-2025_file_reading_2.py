content =  open("hello_kitty.txt","r")

data = content.read()

print(data)


content =  open("hello_kitty.txt","w")

#We write into the file
content.write("My name is Samone Cook \n")
content.write("I like to drink boba tea \n")
content.write("I hate warm weather \n")
content.write("I go to college in Oklahoma \n")

#close the file
content.close()



