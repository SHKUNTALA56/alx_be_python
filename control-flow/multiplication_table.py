# Prompt the user for a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Generate and print the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

