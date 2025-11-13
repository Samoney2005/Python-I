
try:
    content =  open("hello_kitt.txt","r")


except FileNotFoundError:
    print("The file does not exist")
    content =  open("hello_kitt.txt","w")


else:

    
    
    

'''
#open("hello_kitty.txt","r")


 #We write into the file
content.write("Hello Kitty is the best \n")
content.write("She likes coffe \n")
content.write("She hates the cold like me \n")
content.write("She wants to go to college \n")

#close the file
content.close()
'''
