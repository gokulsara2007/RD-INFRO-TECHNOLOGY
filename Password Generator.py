import random
import string
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
while True:
    print("\n=== Password Generator ===")
    print("1. Generate Password")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        try:
            length = int(input("Enter desired password length: "))
            result = generate_password(length)
            print("Generated Password:", result)
        except ValueError:
            print("Invalid input! Please enter a number.")
    elif choice == '2':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")
