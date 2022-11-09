import secrets
import string

alphabet=string.ascii_letters + string.digits + string.punctuation
print("Welcome!")
print("This program generates a password , based on user input ")
# fix password length(read from user input)
print("How many characters you want?")
pwd_length=int(input())
# generate a password string
pwd=''
for i in range(pwd_length):
    pwd+=''.join(secrets.choice(alphabet))

print("Here's your password")
print(pwd)
