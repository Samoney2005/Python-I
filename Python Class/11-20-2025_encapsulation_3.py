class UserAccount:

    #constructor //object

    def __init__(self, username, password):
        self.username = username #public
        self.__password = password #private
        #self._address = address #protected


    #This is a getter
    #@property
    def verify(self):
        return self.__password

    #This is a setter
    #We can modify a private attribute
    def change(self, pwd):
        self.__password = pwd
        


#create object
acc = UserAccount("Sam", 12345)


print(f"Before changes: {acc.username}")

#We make a change here
acc.username = "Mike"

print(f"After changes: {acc.username}")

#print(f"The password is: {acc.password}")
#print(f"The password is: {acc.password}") # Works when attribute is public

print(f"The password is: {acc.verify()}")


print(f"Before changes: {acc.verify()}")

#We make a change here
acc.password = 789456

print(f"After changes: {acc.verify()}")


print(f"Before changes - last: {acc.verify()}")

acc.change(9574239)

print(f"After changes - last: {acc.verify()}")
