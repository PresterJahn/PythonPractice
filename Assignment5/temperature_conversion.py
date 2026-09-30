def main():
    temp_type = input("Enter the type of temperature (F for farenheit or C for celcius)").upper()

    while temp_type != "F" and temp_type != "C":
        print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
        temp_type = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ").upper()

    temperature = float(input("Enter the temperature you want to convert: "))

    if temp_type == "F":
        while temperature < -459.67:
            print("Invalid temperature. Please enter a temperature above absolute zero (-459.67).")
            temperature = float(input("Enter the temperature you want to convert: "))

    else:
        while temperature < -273.15:
            print("Invalid temperature. Please enter a temperature above absolute zero (-273.15).")
            temperature = float(input("Enter the temperature you want to convert: "))

    if temp_type == "F":
        converted_temp = fahrenheit_to_celsius(temperature)
        print(f"The temperature in Celsius is: {converted_temp:.2f}")

    else:
        converted_temp = celsius_to_fahrenheit(temperature)
        print(f"The temperature in Fahrenheit is: {converted_temp:.2f}")

def fahrenheit_to_celsius(temperature):
    celsius = (temperature - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(temperature):
    fahrenheit = temperature * 9 / 5 + 32
    return fahrenheit

if __name__ == "__main__":
    main()
