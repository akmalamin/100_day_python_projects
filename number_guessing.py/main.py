"""
Number Guessing Game
A simple game where the computer picks a random number
and the player tries to guess it with hints.
"""

import random


def set_difficulty():
    """
    Ask user for difficulty level and return game settings.

    Returns:
        tuple: (min_number, max_number, max_attempts)
    """
    print("\nChoose difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return 1, 10, 5
    elif choice == "2":
        return 1, 50, 7
    else:
        return 1, 100, 10


def play_game():
    """
    Play one round of the number guessing game.
    """
    # Get difficulty settings
    min_num, max_num, max_attempts = set_difficulty()

    # Generate secret number
    secret_number = random.randint(min_num, max_num)

    # Initialize game variables
    attempts = 0
    guessed_correctly = False

    print(f"\n🎯 I'm thinking of a number between {min_num} and {max_num}!")
    print(f"You have {max_attempts} attempts to guess it.\n")

    # Main game loop
    while attempts < max_attempts:
        # Get user guess
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")

        # Convert to integer with error handling
        try:
            guess = int(guess_input)
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        # Increment attempts
        attempts += 1

        # Check guess
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            guessed_correctly = True
            break
        elif guess < secret_number:
            print("⬆️  Too low! Try a higher number.")
        else:
            print("⬇️  Too high! Try a lower number.")

        # Show remaining attempts
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Remaining attempts: {remaining}\n")

    # After loop ends
    if not guessed_correctly:
        print(f"\n😔 Sorry, you've used all {max_attempts} attempts!")
        print(f"The secret number was: {secret_number}")


def main():
    """
    Main program loop.
    """
    print("🎮 Welcome to the Number Guessing Game!")
    print("Can you guess the secret number?")

    play_again = "y"

    while play_again.lower() == "y":
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ")

    print("\n👋 Thanks for playing! Goodbye!")


if __name__ == "__main__":
    main()