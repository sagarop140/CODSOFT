import random
import string 

try:
    length = int(input("enter the desire length of password:"))
    characters= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range (length))
    print("generated password:",password)

except ValueError:
    print("invalid input.please enter a positive integer.")