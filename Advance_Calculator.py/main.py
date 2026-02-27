# Advanced Calculator

def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	return a / b


operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}


def main():
	# FIX 1: Move 'a' inside the function (scope issue)
	a = float(input("Enter first number: "))

	while True:
		# Get operation symbol
		operation_symbol = input("Enter operation (+, -, *, /): ").strip()

		# Validate operation exists before retrieving
		if operation_symbol not in operations:
			print(f"❌ Invalid operation '{operation_symbol}'. Choose from: {', '.join(operations.keys())}")
			continue  # Skip to next iteration

		# Safely retrieve function
		calc_function = operations[operation_symbol]

		# Get second number
		b = float(input("Enter second number: "))

		# Execute and display result
		result = calc_function(a, b)
		print(f"Result: {a} {operation_symbol} {b} = {result}")

		# FIX 2: Move continue prompt INSIDE the loop
		continue_input = input("Do you want to continue? (Y/N): ").strip().upper()

		# FIX 3: Use proper variable name (don't shadow 'input' builtin)
		if continue_input == "Y":
			a = result  # Update 'a' for next calculation
		else:
			# FIX 4: Break from inside the loop
			print("Goodbye!")
			break


# FIX 5: Call the main function
if __name__ == "__main__":
	main()