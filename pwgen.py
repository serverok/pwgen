#!/usr/bin/python

"""pwgen: Generate secure password."""

__author__      = "SERVEROK"
__email__       = "admin@serverok.in"
__copyright__   = "Copyright 2016, ServerOk Software"


import random

PASSWORD_LENGTH = 14
password_chars = "abcdefghjkmnpqrstuvwxyz234567890"

def update_password(password, char):
    replace_index = random.randrange(len(password)-1)
    if (replace_index == 0):
        replace_index = 3;
    return password[0:replace_index] + str(char) + password[replace_index+1:]

my_password = ""
have_number = False

for i in range(PASSWORD_LENGTH):
    next_index = random.randrange(len(password_chars))
    if (i < 2):
        next_index = random.randrange(10)
        my_char = password_chars[next_index].upper()
    elif (random.randrange(10) > 5):
        my_char = password_chars[next_index].upper()
    else:
        my_char = password_chars[next_index]
    if i == 12:
        if not have_number:
            my_char =  str(random.randrange(0,9))
    if my_char.isdigit():
        have_number = True;
    my_password = my_password + my_char

#my_password = update_password(my_password, "@")
#my_password = update_password(my_password, random.randrange(0,9))

print my_password
