# multiplication_table.py

# Prompt the user to enter a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print the multiplication table using a for loop
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
