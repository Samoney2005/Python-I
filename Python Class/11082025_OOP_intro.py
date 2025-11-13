
#class creation
class Car:
    


    def drive(self):
        print("The car is driving")


    def brake(self):
        print("The car is braking")

#object creation

honda =  Car()
kia = Car()
toyota = Car()

#add car's data


honda.speed = 50
kia.speed = 20
toyota.speed = 100

print(honda.drive())
print(honda.speed)

print(toyota.drive())

print(kia.drive())

print(honda.brake())
print(toyota.brake())
print(kia.brake())
