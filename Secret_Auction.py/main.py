"""
Secret Auction Program
A silent auction where bidders don't see each other's bids.
Uses simple screen clearing with newlines for cross-platform compatibility.
"""


def find_highest_bidder(bidding_dictionary):
	"""
	Find and display the highest bidder from the bidding dictionary.

	Args:
		bidding_dictionary (dict): Dictionary with bidder names as keys and bid amounts as values
	"""
	winner = ""
	highest_bid = 0

	for bidder in bidding_dictionary:
		bid_amount = bidding_dictionary[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder

	print("\n" + "=" * 50)
	print(f"🎉 THE WINNER IS {winner.upper()}! 🎉")
	print(f"With a bid of ${highest_bid:.2f}")
	print("=" * 50)


def clear_screen():
	"""Clear the console screen using newlines (cross-platform compatible)."""
	print("\n" * 50)


def main():
	"""Main auction program."""
	clear_screen()
	print("=" * 50)
	print("🎵 WELCOME TO THE SECRET AUCTION 🎵")
	print("=" * 50)
	print("Bidders will not see each other's bids.\n")

	auction = {}
	continue_bidding = True

	while continue_bidding:
		# Get bidder name
		name = input("What is your name?: ").strip()
		while not name:
			print("❌ Name cannot be empty. Please try again.\n")
			name = input("What is your name?: ").strip()

		# Get bid amount with validation
		while True:
			try:
				bid_input = input("What is your bid?: $").strip()
				bid_amount = float(bid_input)
				if bid_amount <= 0:
					print("❌ Bid must be greater than $0. Please try again.\n")
					continue
				break
			except ValueError:
				print("❌ Invalid amount. Please enter a number.\n")

		# Add bid to auction
		auction[name] = bid_amount
		print(f"\n✓ Bid recorded for {name}: ${bid_amount:.2f}\n")

		# Ask if more bidders
		while True:
			should_continue = input("Are there any other bidders? (y/n): ").lower().strip()
			if should_continue in ['y', 'n', 'yes', 'no']:
				break
			print("❌ Please enter 'y' or 'n'\n")

		# Handle next steps
		if should_continue in ['y', 'yes']:
			clear_screen()
			print("=" * 50)
			print("🎵 SECRET AUCTION - Next Bidder 🎵")
			print("=" * 50 + "\n")
		else:
			continue_bidding = False

	# Reveal winner on clean screen
	clear_screen()
	find_highest_bidder(auction)
	print("\n👋 Thank you for using the Secret Auction!")


if __name__ == "__main__":
	main()