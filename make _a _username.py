"""
Make a Username
Create a username and initials from a first and last name.

Instructions
Read a first name and a last name from input.

Create a username by joining the two names together in lowercase (no space between them).

Print these two lines:

Username: [username]
Initials: [first letter of first name][first letter of last name] (in uppercase)
"""


first_name = input().strip().lower()
last_name = input().strip().lower()


username = first_name + last_name

initials = first_name[0].capitalize() + last_name[0].capitalize()

#print the output
print("Username:",username)
print("Initials:",initials)
