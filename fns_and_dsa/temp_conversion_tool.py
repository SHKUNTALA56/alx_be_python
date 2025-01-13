# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            if unit.upper() == "C":
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
            elif unit.upper() == "F":
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            else:
                raise ValueError("Invalid unit. Please enter C or F.")
        except ValueError as e:
            print(str(e))

if __name__ == "__main__":
    main()
