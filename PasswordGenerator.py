import random
import string

def generate_password(nr_letters, nr_symbols, nr_numbers, include_special_chars=True):
    letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = string.digits         # '0123456789'
    symbols = '!#$%&()*+'

    if include_special_chars:
        characters = letters + numbers + symbols
    else:
        characters = letters + numbers
    
    # Validate total length of password
    total_length = nr_letters + nr_symbols + nr_numbers
    if total_length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    # Generate password using random.choices for better readability
    password_list = []

    password_list.extend(random.choices(letters, k=nr_letters))
    password_list.extend(random.choices(symbols, k=nr_symbols))
    password_list.extend(random.choices(numbers, k=nr_numbers))

    # Shuffle the password list for better security
    random.shuffle(password_list)

    # Join the shuffled list into a string
    password = ''.join(password_list)

    return password

def main():
    print("Welcome to the Enhanced PyPassword Generator!")

    try:
        nr_passwords = int(input("How many passwords would you like to generate?\n"))
    except ValueError:
        print("Invalid input. Defaulting to generate 1 password.")
        nr_passwords = 1

    passwords = []

    for _ in range(nr_passwords):
        while True:
            try:
                nr_letters = int(input("How many letters would you like in your password?\n"))
                nr_symbols = int(input("How many symbols would you like?\n"))
                nr_numbers = int(input("How many numbers would you like?\n"))
                include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
                password = generate_password(nr_letters, nr_symbols, nr_numbers, include_special_chars)
                passwords.append(password)
                break
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                print("\nOperation aborted by user.")
                return

    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")

if __name__ == "__main__":
    main()
