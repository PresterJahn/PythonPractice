# Constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15

# User input
temperature = float(input("Enter the temperature you want to convert: "))
temperature_type = input(
    "Enter the type of temperature (F for Fahrenheit, C for Celsius): "
)

# Checks for specific temperature type
if temperature_type == "F":

    # Checks for absolute zero
    if temperature >= ABSOLUTE_ZERO_F:
        celsius = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {celsius:.2f}")

    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")

elif temperature_type == "C":

    # Checks for absolute zero
    if temperature >= ABSOLUTE_ZERO_C:
        fahrenheit = temperature * 9 / 5 + 32
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")

    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")

else:
    print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")