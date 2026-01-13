from generator import PasswordGenerator
from validator import PasswordValidator

def main():
    generator = PasswordGenerator()
    validator = PasswordValidator()

    while True:
        print("\n=== Password System ===")
        print("1. Generate Password")
        print("2. Validate Password")
        print("3. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                try:

                    length = int(input("Enter password length: "))
                    password = generator.generate(length)
                    print(f"Generated Password: {password}")
                except ValueError as e:
                    print(f"Error: {e}")

            case "2":
                password = input("Enter password to validate: ")
                rules = validator.validate(password)

                print("\nPassword Rules: ")
                for rule, passed in rules.items():
                    print(f"{rule.capitalize()}: {'✔️' if passed else '❌'}")

                if validator.is_strong(password):
                    print("\nPassword is STRONG")
                else:
                    print("\nPassword is WEAK")

            case "3":
                print("Exiting System.")
                break

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()



            