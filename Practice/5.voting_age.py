"""
Voting Age:
Determine if a person is old enough to vote.
____________________________________________

"""

var_name = input("Enter your name:")
var_age = int(input("Enter your age:"))

if var_age >= 18:
    print(var_name, "can vote")

else:
    print(var_name, "cannot vote")