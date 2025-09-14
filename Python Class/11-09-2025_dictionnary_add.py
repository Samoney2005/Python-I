name = "Sam" #variable
state = ["Virginia", "MD", "TX", "CT"] #list
state2 = {"Virginia": "Richmond", "MD": "Annapolis", "Louisianna": "Baton rouge"} #Dictionnary
country = {"France": "Paris", "Italy": "Roma", "Portugal":"Lisbon"}

print(state)
print(state2)

print(country['Italy'])

travel = country['Italy']

print(f"You travelled to {travel}")

country.update({"Germany": "Berlin"})


print(country)
