import random
import string
import platform
import pyperclip
import configparser

CONFIG_FILE = 'password_generator_config.ini'

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

def load_preferences(config):
    try:
        config.read(CONFIG_FILE)
        if 'Preferences' in config:
            preferences = config['Preferences']
            include_letters = preferences.getboolean('include_letters')
            include_digits = preferences.getboolean('include_digits')
            include_punctuation = preferences.getboolean('include_punctuation')
            length = preferences.getint('length')
            return include_letters, include_digits, include_punctuation, length
    except (configparser.Error, FileNotFoundError):
        # If there's an error reading the config or file not found, return None
        pass

    # Default values in case of an error
    return None

def save_preferences(config, include_letters, include_digits, include_punctuation, length):
    config['Preferences'] = {
        'include_letters': str(include_letters),
        'include_digits': str(include_digits),
        'include_punctuation': str(include_punctuation),
        'length': str(length)
    }
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def get_user_preferences():
    include_letters = input("Include letters? (y/n): ").lower()
    include_digits = input("Include digits? (y/n): ").lower()
    include_punctuation = input("Include punctuation? (y/n): ").lower()

    # Validate user input
    if include_letters not in ['y', 'n'] or include_digits not in ['y', 'n'] or include_punctuation not in ['y', 'n']:
        raise ValueError("Invalid input. Please enter 'y' or 'n'.")

    return include_letters == 'y', include_digits == 'y', include_punctuation == 'y', length


def main():
    config = configparser.ConfigParser()

    while True:
        try:
            # Load preferences
            preferences = load_preferences(config)

            if preferences is None:
                # If preferences are not loaded, get new preferences from the user
                print("No saved preferences found. Please provide new preferences.")
                include_letters, include_digits, include_punctuation, length = get_user_preferences()
            else:
                # Display existing preferences
                include_letters, include_digits, include_punctuation, length = preferences
                print(f"Current Preferences:\n"
                      f"Include letters: {include_letters}\n"
                      f"Include digits: {include_digits}\n"
                      f"Include punctuation: {include_punctuation}\n"
                      f"Password length: {length}")

                # Ask the user if they want to change preferences
                change_preferences = input("Do you want to change preferences? (y/n): ").lower() == 'y'
                if change_preferences:
                    include_letters, include_digits, include_punctuation, length = get_user_preferences()

            # Save preferences
            save_preferences(config, include_letters, include_digits, include_punctuation, length)

            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                raise ValueError("Please enter a positive integer for the number of passwords.")

            for _ in range(num_passwords):
                password = generate_password(length, include_letters, include_digits, include_punctuation)
                print(f"Generated Password: {password}")

                copy_option = input("Do you want to copy the password to clipboard? (y/n): ").lower()
                if copy_option == 'y':
                    copy_to_clipboard(password)

            # Ask the user if they want to generate passwords again or exit
            generate_again = input("Do you want to generate passwords again? (y/n): ").lower()
            if generate_again != 'y':
                break  # Exit the loop and end the script

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
