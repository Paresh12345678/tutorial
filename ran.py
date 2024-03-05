import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    """
    Generate a random password of specified length with specified character types.
    """
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Please choose at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    include_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_letters, include_numbers, include_symbols)

    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()
