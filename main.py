import random
import string
import platform
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    try:
        pyperclip.copy(password)
        print("Password copied to clipboard.")
    except pyperclip.PyperclipException:
        print("Copying to clipboard is not supported on your system.")

def main():
    try:
        length = int(input("Enter the number of characters for the password: "))
        if length <= 0:
            raise ValueError("Please enter a positive integer for the length.")
        
        password = generate_password(length)
        print(f"Generated Password: {password}")

        copy_option = input("Do you want to copy the password to clipboard? (y/n): ").lower()
        if copy_option == 'y':
            copy_to_clipboard(password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
