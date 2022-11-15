import secrets
import string
import pyinputplus

alphabet = string.ascii_letters + string.digits + string.punctuation
print("Welcome!")
print("This program generates a password , based on user input ")
# fix password length(read from user input)
print("How many characters you want?")
print("(Please enter digits only)")
# inputInt will only accept integer , it won't proceed otherwise
pwd_length = (pyinputplus.inputInt())


# generate a password string
pwd = ''
for i in range(pwd_length):
    # keep choosing from values in alphabet until it equals pwd_length
    pwd += ''.join(secrets.choice(alphabet))

print("Here's your password")
print(pwd)
