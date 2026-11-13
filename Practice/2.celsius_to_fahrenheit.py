"""
Celsius to Fahrenheit
Convert a temperature from Celsius to Fahrenheit.
__________________________________________________
Instructions:
Read a temperature in Celsius from input.

Use this formula:

fahrenheit = celsius * 9/5 + 32

Print the result like this:

[celsius] Celsius = [fahrenheit] Fahrenheit

"""

#Data input
celsius = int(input("Enter temprature in celsius:")).strip()

#Conversion
fahrenheit = celsius * 9/5 + 32

#Print Output
print(celsius, "Celsius = ", fahrenheit, "Fahrenheit" )
