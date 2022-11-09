import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
print("Welcome!")
print("This program generates a password , based on user input ")
# fix password length(read from user input)
print("How many characters you want?")
# whatever read from input, is equal to password length
pwd_length = int(input())
# generate a password string
pwd = ''
# for loop, range of loop equals to pwd_length, which is taken from user input 
for i in range(pwd_length):
    #join the empty pwd string with whatever secrets.choice generates from alphabet
    #alphabet will contain letters,digits and punctuations(special characters like */-+ etc. )
    pwd += ''.join(secrets.choice(alphabet))

print("Here's your password")
print(pwd)
