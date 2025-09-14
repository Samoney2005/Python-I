#secret number declaration

secret = 15

guess = 0 #declaration for guess


#loop while secret number different from entered number:
      #enter a guess number

while guess != secret:
    guess = int(input("What's the secret number?"))

print(f"You found the secret number which is {guess}")

#display You found the number
