"""
Hangman Game
A classic word-guessing game with ASCII art hangman.
"""

import random

# Hangman ASCII art stages (7 stages: 0 to 6 wrong guesses)
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

# Word list
word_list = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "london", "laptop", "python", "computer",
             "keyboard"]


def main():
    """Main game function."""
    print("🎮 Welcome to Hangman!")
    print("Guess the word before the hangman is complete.\n")

    play_again = "y"

    while play_again.lower() == "y":
        # Choose random word
        chosen_word = random.choice(word_list)

        # Initialize game variables
        lives = 6
        guessed_letters = []
        display = ["_"] * len(chosen_word)
        game_over = False

        # Game loop
        while not game_over:
            # Display current state
            print(stages[lives])
            print(" ".join(display))
            print(f"Lives remaining: {lives}")
            if guessed_letters:
                print(f"Guessed letters: {', '.join(guessed_letters)}")
            print("-" * 40)

            # Get guess
            guess = input("Guess a letter: ").lower()

            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter a single letter!\n")
                continue

            # Check if already guessed
            if guess in guessed_letters:
                print(f"⚠️  You already guessed '{guess}'!\n")
                continue

            # Add to guessed letters
            guessed_letters.append(guess)

            # Check if guess is correct
            if guess in chosen_word:
                print(f"✅ Good guess! '{guess}' is in the word.\n")

                # Reveal letter in display
                for position in range(len(chosen_word)):
                    if chosen_word[position] == guess:
                        display[position] = guess
            else:
                print(f"❌ Wrong! '{guess}' is not in the word.\n")
                lives -= 1

            # Check win condition
            if "_" not in display:
                print("🎉 YOU WIN!")
                print(f"The word was: {chosen_word.upper()}")
                game_over = True

            # Check lose condition
            elif lives == 0:
                print(stages[0])
                print("💀 GAME OVER!")
                print(f"The word was: {chosen_word.upper()}")
                game_over = True

        # Ask to play again
        print("\n" + "=" * 40)
        play_again = input("Play again? (y/n): ")
        print("=" * 40)

    print("\n👋 Thanks for playing Hangman!")


if __name__ == "__main__":
    main()