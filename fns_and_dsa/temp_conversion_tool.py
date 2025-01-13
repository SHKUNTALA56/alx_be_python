# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Conversion Tool!")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            temp = input("Enter temperature in Celsius: ")
            if not temp.replace('.', '', 1).isdigit():
                print("Invalid temperature. Please enter a numeric value.")
                return
            celsius = float(temp)
            print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
        elif choice == 2:
            temp = input("Enter temperature in Fahrenheit: ")
            if not temp.replace('.', '', 1).isdigit():
                print("Invalid temperature. Please enter a numeric value.")
                return
            fahrenheit = float(temp)
            print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
