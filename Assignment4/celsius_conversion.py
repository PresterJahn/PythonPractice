celsius_degree = int(input("Enter a celsius degree: "))

# Validate the input
while celsius_degree < -273:
    print("Error: temperature cannot be below absolute zero")
    celsius_degree = int(input("Enter a celsius degree: "))

print("Celsius\t\tFahrenheit")
print("------------------------------")

#converts celsius to fahrenheit
for celsius in range(0, celsius_degree + 1):
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, "\t\t", fahrenheit)