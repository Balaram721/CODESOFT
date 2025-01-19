import random
import string

def password_generator():
    print("\n--- Random Password Generator ---")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4 characters. Please enter again.")
                continue

            print("\nChoose the password complexity level:")
            print("1. Letters only")
            print("2. Letters and digits")
            print("3. Letters, digits, and special characters")
            complexity = input("Enter your choice: ")

            if complexity == '1':
                chars = string.ascii_letters
            elif complexity == '2':
                chars = string.ascii_letters + string.digits
            elif complexity == '3':
                chars = string.ascii_letters + string.digits + string.punctuation
            else:
                print("Invalid complexity choice! Please enter again.")
                continue

            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"\nGenerated Password: {password}")

            another = input("\nDo you want to generate another password? (yes/no): ").lower()
            if another != 'yes':
                print("Thank you for using the Password Generator.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

password_generator()