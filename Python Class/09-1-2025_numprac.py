numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_odd_numbers = 0
found_seven = False

for num in numbers:
    # Check if the number is even and skip it
    if num % 2 == 0:
        print(f"Skipping even number: {num}") # Added print statement
        continue 

    # Check if the number exceeds 7 and break the loop
    if num > 7:
        print(f"Breaking loop as {num} exceeds 7.") # Added print statement
        break 

    # Process odd numbers less than or equal to 7
    print(f"Processing odd number: {num}") 
    sum_of_odd_numbers += num # Accumulate sum of odd numbers

    # Check for a specific value
    if num == 7:
        found_seven = True
        print("Found the number 7!")

# After the loop, print accumulated results
print(f"\nSum of processed odd numbers: {sum_of_odd_numbers}")
if found_seven:
    print("The number 7 was found during processing.")
else:
    print("The number 7 was not found (or the loop broke before reaching it).")

# Example of using 'else' with a for loop (executes if loop completes without 'break')
print("\nDemonstrating 'else' with a for loop:")
for i in range(3):
    print(f"Iteration {i}")
else:
    print("Loop completed without a 'break'.")

print("\nDemonstrating 'else' with a 'break' in a for loop:")
for i in range(5):
    if i == 2:
        print(f"Breaking at {i}")
        break
    print(f"Iteration {i}")
else:
    print("This 'else' block will not execute because of 'break'.")
