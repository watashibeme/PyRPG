import os
import secrets
import string
import sys
import time
import platform
import pyinputplus
import xerox


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


alphabet = string.ascii_letters + string.digits + string.punctuation
osdetect = platform.system() + platform.release()
print("Welcome!" + "We have detected that your OS is " + osdetect + "\n later we will use this to try to make")
print("auto-copy to clipboard work")
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
xerox.copy(pwd)
print("password has been copied to clipboard!")
print("do you want to generate another password? t(rue) / f(alse)")
answer = pyinputplus.inputBool()


if answer:
    print("the program now will restart in 3 seconds")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    # now, to clear the screen
    cls()
    os.execl(sys.executable, sys.executable, *sys.argv)

else:
    print("program has ended!")
    exit()
    cls()
