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


#create object
acc = UserAccount("Sam", 12345)


print(f"Before changes: {acc.username}")

#We make a change here
acc.username = "Mike"

print(f"After changes: {acc.username}")

#print(f"The password is: {acc.password}")
#print(f"The password is: {acc.password}") # Works when attribute is public

print(f"The password is: {acc.verify()}")


print(f"Before changes: {acc.password}")

#We make a change here
acc.password = 789456

print(f"After changes: {acc.password}")
