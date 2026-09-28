# prompt the user for a temperature in Fahrenheit
fahrenheit = float(input("Please enter a degree in fahrenheit: "))

# perform the conversion to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# generate the output using f-string to format the result
print(f"{fahrenheit} degrees fahrenheit is {celsius:.2f} degrees celcius")