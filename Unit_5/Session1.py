# Problem 1: Pokemon Class
# Understand: We need to create an object (an instance) from the Pokemon class blueprint.
# This object should represent a specific Pokemon, Pikachu, with the type "Electric".
# Plan: Call the class like a function, passing the required arguments ("Pikachu", ["Electric"])
# to the __init__ method. Store the created object in a variable named my_pokemon.
# Implement:

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
my_pokemon = Pokemon('Pikachu',['Electric'])
print(my_pokemon.name)
print(my_pokemon.types) 
################################################################################

# Problem 2: Create Squirtle
# Understand: We need to create a new Pokemon instance for Squirtle and then
# use the print_pokemon method defined in the class to display its details.
# Plan: 
# 1. Instantiate a new Pokemon object with the name "Squirtle" and type ["Water"]. Store it in a variable called squirtle.
# 2. Call the print_pokemon method on the squirtle object using dot notation.
# Implement:

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
squirtle = Pokemon("Squirtle", ["water"])
squirtle.is_caught = False
squirtle.print_pokemon()

################################################################################

# Problem 3: Is Caught
# Understand: We need to modify an existing attribute of the squirtle object.
# The 'is_caught' attribute should be changed from its default False to True.
# Then, we need to print the object's data to verify the change.
# Plan:
# 1. Access the is_caught attribute directly on the squirtle instance using dot notation (squirtle.is_caught).
# 2. Assign the new value, True, to this attribute.
# 3. Call the print_pokemon() method on squirtle again to see the updated information.
# Implement:

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
squirtle = Pokemon("Squirtle", ["water"])
squirtle.is_caught = True 
squirtle.print_pokemon()
################################################################################

# Problem 4: Catch Pokemon
# Understand: We need to add a new capability (a method) to the Pokemon class
# called 'catch'. This method should change the is_caught status to True.
# Plan:
# 1. Define a new function inside the Pokemon class named 'catch'. It must take 'self' as its first parameter.
# 2. Inside this method, access the instance's is_caught attribute using 'self.is_caught'.
# 3. Assign the value True to self.is_caught.
# Implement:
#class Pokemon():
def catch(self):
		self.is_caught = True 
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

################################################################################

# Problem 5: Choose Pokemon
# Understand: We need to add a method 'choose' that prints different messages
# based on whether the Pokemon's 'is_caught' attribute is True or False.
# Plan:
# 1. Define a new method 'choose' inside the Pokemon class that takes 'self'.
# 2. Use an if statement to check the boolean value of 'self.is_caught'.
# 3. If it's True, print the "I choose you!" message including the Pokemon's name.
# 4. If it's False (the else case), print the "is wild!" message.
# Implement:
class Pokemon():
	...
	
	def choose(self):
		pass

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

################################################################################

# Problem 6: Add Pokemon Type
# Understand: We need to add a method 'add_type' that can add a new type
# to a Pokemon's existing list of types.
# Plan:
# 1. Define a new method 'add_type' that takes 'self' and a 'new_type' string as parameters.
# 2. Access the list of types using 'self.types'.
# 3. Use the list's built-in .append() method to add the 'new_type' to the list.
# Implement:

class Pokemon():
	...
	
	def add_type(self, new_type):
		pass
	
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon() 


################################################################################

# Problem 7: Get Pokemon
# Understand: We need to write a standalone function (not a class method) that
# filters a list of Pokemon objects and returns a new list containing only those
# that match a specific type.
# Plan:
# 1. Define a function 'get_by_type' that accepts a list 'my_pokemon' and a string 'pokemon_type'.
# 2. Create an empty list to store the results (e.g., 'found_pokemon').
# 3. Loop through each 'pokemon' object in the input list 'my_pokemon'.
# 4. Inside the loop, use an 'if' statement to check if 'pokemon_type' is in the current 'pokemon.types' list.
# 5. If it is, append the entire 'pokemon' object to the 'found_pokemon' list.
# 6. After the loop, return the 'found_pokemon' list.
# Implement:

class Pokemon():
	...
	
def get_by_type(my_pokemon, pokemon_type):
	pass

# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

################################################################################

# Problem 8: Pokemon Evolution
# Understand: We need a function that takes one Pokemon and follows its 'evolution'
# attribute to find all subsequent evolutions, returning them in a list.
# Plan:
# 1. Define a function 'get_evolutionary_line' that accepts a 'starter_pokemon'.
# 2. Create an empty list to store the evolutionary line.
# 3. Create a 'current_pokemon' variable and initialize it with 'starter_pokemon'.
# 4. Use a 'while' loop that continues as long as 'current_pokemon' is not None.
# 5. Inside the loop, add the 'current_pokemon' to our list.
# 6. Then, update 'current_pokemon' to be its own evolution (current_pokemon.evolution) for the next loop iteration.
# 7. When the loop finishes (because an evolution is None), return the list.
# Implement:

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
def get_evolutionary_line(starter_pokemon):
	pass

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)

################################################################################

# Problem 9: Node Class
# Understand: We need to create two separate instances of the Node class.
# One node should hold the value 'a', and the other should hold 'b'.
# Plan:
# 1. Call the Node class constructor with 'a' as the value argument and assign it to 'node_one'.
# 2. Call the Node class constructor with 'b' as the value argument and assign it to 'node_two'.
# Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
    print(node_one.value) 
    print(node_one.next) 
    print(node_two.value)
    print(node_two.next) 

################################################################################

# Problem 10: Linking Nodes
# Understand: We need to connect the two nodes from the previous problem.
# 'node_one' should be the first in the sequence, so its 'next' pointer
# should point to 'node_two'.
# Plan:
# 1. Access the 'next' attribute of the 'node_one' object.
# 2. Assign the 'node_two' object to 'node_one.next'.
# Implement:
print(node_one.value)
print(node_one.next.value)
print(node_two.value)


################################################################################

# Problem 11: Mario Party
# Understand: We need to create a chain of four nodes representing a list
# of names: Mario -> Luigi -> Wario -> Toad.
# Plan: It's easiest to build a linked list backwards.
# 1. Create the last node, 'Toad', which points to None.
# 2. Create the 'Wario' node, and in its constructor, set its 'next' to the 'Toad' node.
# 3. Create the 'Luigi' node, setting its 'next' to the 'Wario' node.
# 4. Create the 'Mario' node (the head), setting its 'next' to the 'Luigi' node.
# Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

################################################################################

# Problem 12: Printing Linked List
# Understand: We need a function that can travel through a linked list from
# its head node and print out each node's value in a specific format.
# Plan:
# 1. Define a function 'print_linked_list' that accepts a 'head' node.
# 2. Create a 'current_node' variable and set it to 'head'.
# 3. Create an empty list to store the string values of each node.
# 4. Use a 'while' loop that runs as long as 'current_node' is not None.
# 5. Inside the loop, append the 'current_node.value' to the list of values.
# 6. Move to the next node by setting 'current_node = current_node.next'.
# 7. After the loop, use the string '.join()' method to combine the list of values with " -> " as the separator.
# 8. Print the final joined string.
# Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	pass

# input linked list: a->b->c->d->e
print_linked_list(a)