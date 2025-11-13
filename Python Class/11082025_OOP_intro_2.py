
#class creation
class Car:


    #constructor

    def __init__(self, speed, color):

        self.speed = speed
        self.color = color


    def drive(self):
        print("The car is driving")


    def brake(self):
        print("The car is braking")

#object creation


honda = Car(40, "red")



'''
honda =  Car()
kia = Car()
toyota = Car()

#add car's data



honda.speed = 50
honda.color = "red"
kia.speed = 20
toyota.speed = 100

print(honda.drive())
print(honda.speed)

print(toyota.drive())

print(kia.drive())

'''

print(honda.brake())
print(honda.speed)
print(honda.color)


#print(toyota.brake())
#print(kia.brake())
