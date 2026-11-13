"""
Make a Username
Create a username and initials from a first and last name.
_________________________________________________________________________________________

"""

#Variable
first_name = input().strip().lower()
last_name = input().strip().lower()

#username
username = first_name + last_name

#initials
initials = first_name[0].capitalize() + last_name[0].capitalize()

#print the output
print("Username:",username)
print("Initials:",initials)
