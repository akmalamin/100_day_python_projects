"""
Simple Calculator
A menu-driven calculator that performs basic arithmetic operations.
"""


def add():
    """Add two numbers"""
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"✅ The sum of {x} and {y} is {x + y}")


def sub():
    """Subtract two numbers"""
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"✅ The difference of {x} and {y} is {x - y}")


def mul():
    """Multiply two numbers"""
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"✅ The product of {x} and {y} is {x * y}")


def div():
    """Divide two numbers"""
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if y == 0:
        print("❌ Error: Cannot divide by zero!")
    else:
        print(f"✅ The quotient of {x} and {y} is {x / y}")


def main():
    """Main calculator program"""
    print("🧮 Welcome to Simple Calculator")

    cal_again = "Y"
    while cal_again == "Y":
        print("\n" + "=" * 40)
        print("🧮 CALCULATOR MENU")
        print("=" * 40)
        choice = input("Choose operation (1=add, 2=subtract, 3=multiply, 4=divide): ")

        if choice == "1":
            add()
        elif choice == "2":
            sub()
        elif choice == "3":
            mul()
        elif choice == "4":
            div()
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")

        print("=" * 40)
        cal_again = input("\nCalculate again? (Y/N): ").upper()

    print("\n👋 Goodbye! Thanks for using the calculator!")


if __name__ == "__main__":
    main()