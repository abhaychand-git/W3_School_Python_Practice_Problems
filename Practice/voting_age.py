"""
Voting Age:
Determine if a person is old enough to vote.

Instructions:
Read a name and an age from input.

If the person is 18 or older, print:

[name] can vote
If the person is younger than 18, print:

[name] cannot vote

"""

var_name = input("Enter your name:")
var_age = int(input("Enter your age:"))

if var_age >= 18:
    print(var_name, "can vote")

else:
    print(var_name, "cannot vote")