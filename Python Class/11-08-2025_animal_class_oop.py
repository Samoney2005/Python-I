#class creation


#create an object dog


#attributes (fata or variables) will be: breed, color, name

# when looking at constructor you can match with the data_add

class Animals:
    def __init__(self,breed,color,name):

        self.breed = breed
        self.color = color
        self.name = name

    def bark(self):
        print("The dog is barking")

    def drink(self):
        print("The dog is is drinking")

    def eat(self):
        print("The dog is eating")

    def jump(self):
        print("The dog is jumping")


    

dog1 = Animals("Doberman","Grey","Toby")
print(dog1.name)
print(f'The dogs name is {dog1.name}')
print(dog1.breed)
print(f'The dogs name is {dog1.breed}')
print(dog1.color)
print(f'The dogs name is {dog1.color}')



    
        

        
