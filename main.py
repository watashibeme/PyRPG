import os
import sys
import secrets
import string
import time
import platform
import pyinputplus
import pyperclip
import subprocess
from random import *

alphabet = string.ascii_letters + string.digits + string.punctuation
osdetect = platform.system() + platform.release()
print("what do you want to do? \n "
      "1 - generate a password \n "
      "2 - encrypt / decrypt a sentence")
option = pyinputplus.inputInt()

if option == 1:
    print("Welcome!" + "Your platform is " + osdetect)
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
    pyperclip.copy(pwd)
    print("password has been copied to clipboard!")
    print("do you want to generate another password? t(meaning YES) / f(meaning NO)")
    answer = pyinputplus.inputBool()

    if answer:
        print("the program now will restart in 3 seconds")
        for s in range(3):
            time.sleep(1)
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
                        sys.argv[1:])
    else:
        print("program has ended!")
        exit()

elif option == 2:
    letters = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]
    originallet = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]


    def encrypt():
        text = input("Enter your text: ")
        rand_n = randint(10, 99)

        for i in range(rand_n):
            fakenum = letters[0]
            letters.remove(fakenum)
            letters.append(fakenum)

        finaltext = ""
        for i in text:
            number = originallet.index(i)
            finaltext += letters[number]

        chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", "0", "<", ">", "?", "/", "|", "~"]

        f_text_list = []
        for i in finaltext:
            f_text_list.append(i)

        for i in range(len(f_text_list)):
            char = chars[randint(0, len(chars) - 1)]
            f_text_list.insert(i * 2, char)

        f2_list = f_text_list[::-1]

        rand_s = str(rand_n)

        f2_list.insert(0, rand_s[0])
        f2_list.append(rand_s[1])

        f_text = ""

        for i in f2_list:
            f_text += i
        pyperclip.copy(f_text)
        print(f_text)


    def decrypt():

        ramzide = input("Enter you encrypted text: ")
        num = ""
        num += ramzide[0]
        num += ramzide[len(ramzide) - 1]
        ramz_list = []
        for i in ramzide:
            ramz_list.append(i)
        ramz_list.pop(0)
        ramz_list.pop(len(ramz_list) - 1)

        chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", "0", "<", ">", "?", "/", "|", "~"]
        for i in range(10):
            for i in chars:
                if i in ramz_list:
                    ramz_list.remove(i)

        ramz_list = ramz_list[::-1]

        for i in range(int(num)):
            fakenum = letters[0]
            letters.remove(fakenum)
            letters.append(fakenum)

        finaltext = ""
        for i in ramz_list:
            number = letters.index(i)
            finaltext += originallet[number]

        print(finaltext)


    ok = "y"
    while ok == "y":
        choice = input("encrypt or decrypt (e/d) ")

        if choice == "e":
            encrypt()
        elif choice == 'd':
            decrypt()
        else:
            print("its a wrong input")

        ok = input("do you want to continue?? (y/n)")
        letters = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]
