# pattern_drawing.py

# Prompt the user to enter a positive integer for the pattern size
try:
    size = int(input("Enter the size of the pattern: "))
    
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        # Use a while loop for each row
        row = 0
        while row < size:
            # Use a for loop to print asterisks for each column in the row
            for col in range(size):
                print("*", end="")
            # Move to the next line after finishing the row
            print()
            row += 1
except ValueError:
    print("Invalid input. Please enter a positive integer.")
