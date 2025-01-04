# Prompt the user to enter the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Draw the square pattern using nested loops
row = 0  # Initialize row counter for the while loop
while row < size:
    for col in range(size):  # For loop to print asterisks in a row
        print("*", end="")
    print()  # Print newline after each row
    row += 1

