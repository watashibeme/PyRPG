import random
import string
import platform
import pyperclip

def generate_password(length, include_letters=True, include_digits=True, include_punctuation=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be selected.")

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
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            raise ValueError("Please enter a positive integer for the number of passwords.")

        length = int(input("Enter the number of characters for each password: "))
        if length <= 0:
            raise ValueError("Please enter a positive integer for the length.")

        include_letters = input("Include letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

        for _ in range(num_passwords):
            password = generate_password(length, include_letters, include_digits, include_punctuation)
            print(f"Generated Password: {password}")

            copy_option = input("Do you want to copy the password to clipboard? (y/n): ").lower()
            if copy_option == 'y':
                copy_to_clipboard(password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
