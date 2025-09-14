FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(temp):
    converted_temp = (temp - 32) *  FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temp}°F is {converted_temp}°C")

def convert_to_fahrenheit(temp):
    converted_temp = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) +32
    print(f"{temp}°C is {converted_temp}°F")

temp = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    convert_to_fahrenheit(temp)
else:
    convert_to_celsius(temp)