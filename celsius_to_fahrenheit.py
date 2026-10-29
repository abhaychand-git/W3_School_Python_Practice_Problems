"""
Celsius to Fahrenheit
Convert a temperature from Celsius to Fahrenheit.

Instructions:
Read a temperature in Celsius from input.

Use this formula:

fahrenheit = celsius * 9/5 + 32

Print the result like this:

[celsius] Celsius = [fahrenheit] Fahrenheit

"""


celsius = int(input("Enter temprature in celsius:")).strip()

fahrenheit = celsius * 9/5 + 32

print(celsius, "Celsius = ", fahrenheit, "Fahrenheit" )