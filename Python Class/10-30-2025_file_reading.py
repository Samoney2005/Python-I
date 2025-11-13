content =  open("hello_kitty.txt","r")

data = content.read()

print(data)

content.close()

'''

 #We write into the file
content.write("Hello Kitty is the best \n")
content.write("She likes coffe \n")
content.write("She hates the cold like me \n")
content.write("She wants to go to college \n")

#close the file
content.close()


'''
