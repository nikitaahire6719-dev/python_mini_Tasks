import random

def play_level(level, max_number, attempts):
    secret = random.randint(1, max_number)
    print(f"\nLevel {level}")
    print(f"Guess a number between 1 and {max_number}")
    print(f"You have {attempts} attempts")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input("Attempt {attempt}: "))
        except ValueError:
            print("Enter a valid number")
            continue
        if guess == secret:
            print("Correct! Level Cleared. ")
            return True
        elif guess < secret:
            print(" Too low")
        else:
            print("Too high")

    print(f"out of attempts! The number was {secret}")
    return False

def main():
    levels = [
        (1, 10, 5),
        (2, 20, 5),
        (3, 50, 6),
        (4, 100, 7)
    ]
    print("Number Guessing Game")

    for level, max_number, attempts in levels:
        if not play_level(level, max_number, attempts):
            print("\n Game Over")
            break
        else:
            print("\n Congratulations! you completed all levels.")

if __name__ == "__main__":
    main()