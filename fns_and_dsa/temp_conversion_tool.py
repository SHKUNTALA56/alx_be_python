# Constants for conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

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
    Main function to handle temperature conversion.
    """
    print("Temperature Conversion Tool")

    while True:
        print("\nOptions:")
        print("1. Convert a Temperature")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                # Prompt user for temperature to convert
                temperature = float(input("Enter the temperature to convert: ").strip())
                # Prompt user to specify the temperature unit
                unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

                if unit == 'C':
                    converted = celsius_to_fahrenheit(temperature)
                    print(f"{temperature}°C is equal to {converted}°F.")
                elif unit == 'F':
                    converted = fahrenheit_to_celsius(temperature)
                    print(f"{temperature}°F is equal to {converted}°C.")
                else:
                    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            except ValueError:
                print("Invalid input. Please enter a valid numerical temperature.")
        elif choice == '2':
            print("Exiting the Temperature Conversion Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select '1' or '2'.")

if __name__ == "__main__":
    main()
