"""
Quiz Game
A multiple-choice quiz game with difficulty levels and scoring.
"""

# Quiz questions database
QUIZ_QUESTIONS = {
    "easy": [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippo"],
            "answer": "Blue Whale"
        },
        {
            "question": "How many continents are there?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        }
    ],
    "medium": [
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "answer": "Pacific"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2", "NaCl"],
            "answer": "H2O"
        },
        {
            "question": "Which element has the symbol 'Au'?",
            "options": ["Silver", "Gold", "Aluminum", "Argon"],
            "answer": "Gold"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["6", "7", "8", "9"],
            "answer": "8"
        }
    ],
    "hard": [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Go", "Gd", "Au", "Ag"],
            "answer": "Au"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1943", "1944", "1945", "1946"],
            "answer": "1945"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the value of pi (π) to two decimal places?",
            "options": ["3.14", "3.16", "3.18", "3.20"],
            "answer": "3.14"
        },
        {
            "question": "Which scientist developed the theory of relativity?",
            "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
            "answer": "Albert Einstein"
        }
    ]
}


def display_question(question_data):
    """Display a question and its options."""
    print(f"\n❓ {question_data['question']}")
    print("-" * 40)

    letters = "ABCD"
    for i, option in enumerate(question_data["options"]):
        print(f"{letters[i]}. {option}")


def get_answer():
    """Get user's answer choice."""
    while True:
        answer = input("\nYour answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("❌ Invalid choice! Please enter A, B, C, or D.")


def check_answer(user_choice, question_data):
    """Check if answer is correct."""
    letters = "ABCD"
    index = letters.index(user_choice)
    selected_option = question_data["options"][index]
    return selected_option == question_data["answer"]


def play_quiz(questions):
    """Play the quiz with given questions."""
    score = 0
    total = len(questions)

    print(f"\n📚 Starting quiz with {total} questions!")
    print("=" * 40)

    for i, question in enumerate(questions, start=1):
        print(f"\n📝 Question {i}/{total}")
        display_question(question)

        user_choice = get_answer()

        if check_answer(user_choice, question):
            print("✅ Correct!")
            score += 1
        else:
            letters = "ABCD"
            correct_index = question["options"].index(question["answer"])
            correct_letter = letters[correct_index]
            print(f"❌ Wrong! The correct answer was {correct_letter}. {question['answer']}")

        input("\nPress Enter to continue...")

    # Calculate and show results
    percentage = (score / total) * 100

    print("\n" + "=" * 40)
    print("🎉 QUIZ COMPLETE!")
    print("=" * 40)
    print(f"Final Score: {score}/{total} ({percentage:.1f}%)")

    # Encouraging message
    if percentage >= 90:
        print("🌟 Excellent! Perfect score!")
    elif percentage >= 70:
        print("👍 Great job! You know your stuff!")
    elif percentage >= 50:
        print("📚 Good effort! Keep learning!")
    else:
        print("💪 Better luck next time! Try again!")

    print("=" * 40)

    return score


def choose_difficulty():
    """Let user choose difficulty level."""
    print("\n" + "=" * 40)
    print("📚 Quiz Game")
    print("=" * 40)
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")
    print("=" * 40)

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        return QUIZ_QUESTIONS["easy"]
    elif choice == "2":
        return QUIZ_QUESTIONS["medium"]
    elif choice == "3":
        return QUIZ_QUESTIONS["hard"]
    elif choice == "4":
        return None
    else:
        print("❌ Invalid choice! Defaulting to Easy.")
        return QUIZ_QUESTIONS["easy"]


def main():
    """Main quiz game loop."""
    print("📚 Welcome to Quiz Game!")
    print("Test your knowledge with multiple choice questions.")

    play_again = "y"

    while play_again.lower() == "y":
        questions = choose_difficulty()

        if questions is None:
            break

        play_quiz(questions)

        play_again = input("\nPlay again? (y/n): ")

    print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()