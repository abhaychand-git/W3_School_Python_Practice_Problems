"""
Celsius to Fahrenheit
Convert a temperature from Celsius to Fahrenheit.
__________________________________________________

"""

#Data input
celsius = int(input("Enter temprature in celsius:")).strip()

#Conversion
fahrenheit = celsius * 9/5 + 32

#Print Output
print(celsius, "Celsius = ", fahrenheit, "Fahrenheit" )
