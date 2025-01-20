# Constants for conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: (Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Formula: (Fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    """
    Main function to handle user input for temperature conversions.
    """
    print("Temperature Conversion Tool")
    while True:
        print("\nOptions:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit}°F.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius}°C.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Exiting the Temperature Conversion Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
