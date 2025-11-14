class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def recharge(self):
        print("Go to the gas station!")

'''
    def rental_per_day(self):
        return 50
'''

# class
class ElectricVehicle(Vehicle):

    # method
    def recharge(self):
        print("Please plug your car in the electric plug!")

class Hybrid(Vehicle):
    # method
    def recharge(self):
        print("Go plug your car in or go to the gas station!")


# object
Tesla = ElectricVehicle("Tesla","X",2023)
Benz = Vehicle("Mercedes","GLE", 2021)
Toyota = Hybrid("Toyota","Prius",2020)

# use with the method
Tesla.recharge()

print(Tesla.make)
print(Tesla.year)
print(Tesla.model)

# use with the method
Benz.recharge()

print(Benz.make)
print(Benz.year)
print(Benz.model)

# use with the method
Toyota.recharge()

print(Toyota.make)
print(Toyota.year)
print(Toyota.model)

'''
class Car(Vehicle):

    def rental_per_day(self):
        return 80


class Bike(Vehicle):

    def rental_per_day(self):
        return 20


class Truck(Vehicle):

    def rental_per_day(self):
        return 150


vehicles = [Car("Toyota", "Camry", "1995"), Bike("Harley Davidson", "V-Rod", 2022), Truck("Peterbilt", "370", 1988)]


for item in vehicles:

    print(f"the make of the vehicle is {item.make}")


car2 = Car("Ford", "Fiesta", "2018")

print(car2.rental_per_day())

#car1 = Vehicle("GMC", "Silverado", 2016)

#print(car1.make)
'''