# ========================
# COFFEE MACHINE PROJECT
# Day 15 - 100 Days of Code
# ========================

MENU = {
	"espresso": {
		"ingredients": {
			"water": 50,
			"milk": 0,
			"coffee": 18,
		},
		"cost": 1.5,
	},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 2.5,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 3.0,
	}
}

resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
	"money": 0,
}


def print_report():
	"""Display current resource levels and money earned."""
	print("\n" + "=" * 40)
	print("📊 CURRENT STATUS REPORT")
	print("=" * 40)
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${resources['money']:.2f}")
	print("=" * 40 + "\n")


def is_resource_sufficient(order_ingredients):
	"""
	Check if resources are sufficient for the order.

	Args:
		order_ingredients (dict): Dictionary of required ingredients

	Returns:
		bool: True if sufficient, False otherwise (with error message)
	"""
	for item in order_ingredients:
		if resources[item] < order_ingredients[item]:
			print(f"\n❌ Sorry, there is not enough {item}.")
			return False
	return True


def process_coins():
	"""
	Process coin inputs and calculate total value.

	Returns:
		float: Total monetary value inserted
	"""
	print("\n💰 Please insert coins.")
	quarters = int(input("How many quarters? (25¢): "))
	dimes = int(input("How many dimes? (10¢): "))
	nickels = int(input("How many nickels? (5¢): "))
	pennies = int(input("How many pennies? (1¢): "))
	
	total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
	return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
	"""
	Validate payment and handle change calculation.

	Args:
		money_received (float): Total inserted by user
		drink_cost (float): Cost of selected drink

	Returns:
		bool: True if payment sufficient, False if refunded
	"""
	if money_received < drink_cost:
		print("\n❌ Sorry, that's not enough money. Money refunded.")
		return False
	
	change = round(money_received - drink_cost, 2)
	if change > 0:
		print(f"\n✅ Here is ${change:.2f} in change.")
	
	return True


def make_coffee(drink_name, order_ingredients):
	"""
	Deduct resources and deliver coffee.

	Args:
		drink_name (str): Name of drink to prepare
		order_ingredients (dict): Ingredients required for the drink
	"""
	# Deduct ingredients from resources
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
	
	# Add payment to machine's money (only the drink cost)
	resources["money"] += MENU[drink_name]["cost"]
	
	# Deliver product
	print(f"\n{'=' * 40}")
	print(f"☕ Here is your {drink_name}! Enjoy!")
	print(f"{'=' * 40}\n")


# ========================
# MAIN PROGRAM LOOP
# ========================
def main():
	"""Run the coffee machine program."""
	print("\n" + "=" * 50)
	print("☕ WELCOME TO THE COFFEE MACHINE ☕")
	print("=" * 50)
	
	is_on = True
	while is_on:
		# Get user selection
		choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
		
		# Handle shutdown command
		if choice == "off":
			print("\n" + "=" * 50)
			print("🔌 Machine turning off. Goodbye!")
			print("=" * 50 + "\n")
			is_on = False
		
		# Handle report command
		elif choice == "report":
			print_report()
		
		# Handle drink selection
		elif choice in MENU:
			drink = MENU[choice]
			
			# Check resources BEFORE taking money
			if is_resource_sufficient(drink["ingredients"]):
				# Process payment
				payment = process_coins()
				
				# Validate transaction
				if is_transaction_successful(payment, drink["cost"]):
					# Brew coffee and update state
					make_coffee(choice, drink["ingredients"])
		
		# Handle invalid input
		else:
			print("\n❌ Invalid selection. Please choose espresso, latte, or cappuccino.\n")


# ========================
# PROGRAM ENTRY POINT
# ========================
if __name__ == "__main__":
	main()