import random
from random import choice
import string

#get characters from string library
passwordCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 

#random length for password
minlength = 12
maxlength = 20
length = random.randint(12,20)

#pick up random characters from our list within previous random range
password = print(''.join([choice(passwordCharacters) for _ in range(length)]))