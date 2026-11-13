"""
Multiplication Table:
Print the multiplication table for a given number.

_____________________________________________________
"""

n = int(input("Enter the Number:"))

for i in range(1,11,1):
    print(n, "x", i, "=", i*n)