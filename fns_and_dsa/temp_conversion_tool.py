# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # This line ensures the global factor is defined

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to prompt the user for input, validate it, 
    and perform the appropriate temperature conversion.
    """
    try:
        # Prompt the user for the temperature
        temperature_input = input("Enter the temperature to convert: ")
        temperature = float(temperature_input)  # Convert input to a numeric value

        # Ask for the unit of the input temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the conversion based on the unit
        if unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        # Handle invalid numeric input or invalid unit
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
