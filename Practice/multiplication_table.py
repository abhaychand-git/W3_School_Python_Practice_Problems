"""
Multiplication Table:
Print the multiplication table for a given number.

Instructions:
Read a number from input.

Print its multiplication table from 1 to 10.

Each line should look like this:

[number] x [i] = [result]
"""

n = int(input("Enter the Number:"))

for i in range(1,11,1):
    print(n, "x", i, "=", i*n)