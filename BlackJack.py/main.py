"""
Blackjack Game
A text-based casino Blackjack game where player competes against dealer.
Implements official Blackjack rules with Ace flexibility and Blackjack detection.

Features:
- Authentic Blackjack rules (hit/stand, dealer AI, Ace 1/11 logic)
- Blackjack detection (Ace + 10-value card in first 2 cards)
- Professional formatted output with ASCII art
- Input validation and error handling
- Play again functionality with screen clearing
- Comprehensive win condition logic
- Cross-platform compatible (no external dependencies)

Author: [Your Name]
Date: [Current Date]
"""

import random


def deal_card():
	"""
	Returns a random card from the deck.

	Card values:
	- 11 represents Ace
	- 2-10 represent number cards
	- 10 represents face cards (Jack, Queen, King)

	Returns:
		int: Random card value (1-11)
	"""
	deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(deck)


def calculate_score(hand):
	"""
	Calculate the score of a hand with Ace flexibility and Blackjack detection.

	Ace Handling:
	- Ace counts as 11 unless it causes bust (>21), then converts to 1
	- Converts Aces one at a time while hand is busting

	Blackjack Detection:
	- Returns 0 if hand has exactly 2 cards totaling 21 (Ace + 10-value card)
	- This special value simplifies win condition checks later

	Args:
		hand (list): List of integers representing card values

	Returns:
		int:
			0 if Blackjack (special code),
			sum of cards (with Aces converted if needed) otherwise
	"""
	# Calculate initial score
	score = sum(hand)
	
	# Convert Aces from 11 to 1 while busting
	# Using while loop to handle multiple Aces automatically
	while score > 21 and 11 in hand:
		hand.remove(11)
		hand.append(1)
		score = sum(hand)
	
	# Check for Blackjack (must be exactly 2 cards totaling 21)
	if score == 21 and len(hand) == 2:
		return 0  # Special code for Blackjack
	
	return score


def compare(player_score, dealer_score):
	"""
	Compare scores and determine winner based on Blackjack rules.

	Win Priority (checked in this exact order):
	1. Bust checks (player or dealer over 21)
	2. Blackjack checks (special value 0)
	3. Score comparison (higher score wins)

	Args:
		player_score (int): Player's final score (0 = Blackjack)
		dealer_score (int): Dealer's final score (0 = Blackjack)

	Returns:
		str: Result message with appropriate emoji
	"""
	# Priority 1: Bust checks
	if player_score > 21:
		return "❌ You went over. You lose 😭"
	if dealer_score > 21:
		return "✅ Dealer went over. You win 😁"
	
	# Priority 2: Blackjack checks
	if dealer_score == 0:
		return "❌ Dealer has Blackjack! You lose 😱"
	if player_score == 0:
		return "✅ BLACKJACK! You win 😎"
	if player_score == 0 and dealer_score == 0:
		return "🤝 Both have Blackjack! It's a push 🤯"
	
	# Priority 3: Score comparison
	if player_score == dealer_score:
		return "🤝 It's a push (tie) 🤔"
	if player_score > dealer_score:
		return "✅ You win! 😃"
	return "❌ You lose 😤"


def clear_screen():
	"""Clear console screen using newlines (cross-platform compatible)."""
	print("\n" * 50)


def display_hand(name, hand, hide_second_card=False):
	"""
	Display a player's hand with optional second card hiding.

	Args:
		name (str): Name of the player ("Your" or "Dealer's")
		hand (list): List of card values
		hide_second_card (bool): If True, hide second card (for dealer during player turn)
	"""
	if hide_second_card and len(hand) > 1:
		display_cards = f"[{hand[0]}, ?]"
		score_text = ""
	else:
		display_cards = str(hand)
		score = calculate_score(hand.copy())  # Use copy to avoid modifying original
		score_display = "Blackjack! 🎯" if score == 0 else f"{score if score != 0 else 21}"
		score_text = f" → Score: {score_display}"
	
	print(f"{name} cards: {display_cards}{score_text}")


def play_game():
	"""Main game logic for a single round of Blackjack."""
	# Initialize hands
	player_hand = []
	dealer_hand = []
	
	# Deal initial cards
	for _ in range(2):
		player_hand.append(deal_card())
		dealer_hand.append(deal_card())
	
	# Calculate initial scores
	player_score = calculate_score(player_hand.copy())
	dealer_score = calculate_score(dealer_hand.copy())
	
	# Check for instant Blackjack
	is_game_over = False
	if player_score == 0 or dealer_score == 0:
		is_game_over = True
	
	# Player's turn
	while not is_game_over and player_score <= 21:
		clear_screen()
		print("=" * 60)
		print("♠️ ♥️ ♦️ ♣️  BLACKJACK ♣️ ♦️ ♥️ ♠️".center(60))
		print("=" * 60)
		display_hand("Your", player_hand)
		display_hand("Dealer's", dealer_hand, hide_second_card=True)
		print("=" * 60)
		
		# Get player action
		action = input("\nType 'y' to get another card (hit), 'n' to pass (stand): ").lower()
		
		if action == 'y':
			player_hand.append(deal_card())
			player_score = calculate_score(player_hand.copy())
			if player_score > 21:
				is_game_over = True
		elif action == 'n':
			is_game_over = True
		else:
			print("❌ Invalid input. Please type 'y' or 'n'.")
			input("Press Enter to continue...")
	
	# Dealer's turn (only if player didn't bust)
	if player_score <= 21:
		while dealer_score < 17 and dealer_score != 0:
			dealer_hand.append(deal_card())
			dealer_score = calculate_score(dealer_hand.copy())
	
	# Display final hands
	clear_screen()
	print("=" * 60)
	print("♠️ ♥️ ♦️ ♣️  GAME OVER ♣️ ♦️ ♥️ ♠️".center(60))
	print("=" * 60)
	display_hand("Your final", player_hand)
	display_hand("Dealer's final", dealer_hand)
	print("=" * 60)
	
	# Determine and display result
	result = compare(player_score, dealer_score)
	print(f"\n🏆 RESULT: {result}\n")
	print("=" * 60)


def main():
	"""Main program loop with welcome message and play again functionality."""
	clear_screen()
	print("=" * 60)
	print("♠️ ♥️ ♦️ ♣️  WELCOME TO BLACKJACK! ♣️ ♦️ ♥️ ♠️".center(60))
	print("=" * 60)
	print("""
🎯 HOW TO PLAY:
• Get as close to 21 as possible without going over
• Ace counts as 1 or 11 (automatically optimized)
• Blackjack (Ace + 10-value card) wins automatically
• Dealer must hit until reaching 17 or higher
• Type 'y' to HIT (take another card)
• Type 'n' to STAND (end your turn)

🏆 WIN CONDITIONS:
✅ Blackjack beats regular 21
✅ Higher score than dealer (≤21) wins
✅ Dealer busts (>21) = you win
❌ You bust (>21) = automatic loss
🤝 Same score = push (tie)
    """.strip())
	print("=" * 60)
	
	while True:
		play = input("\n🎲 Ready to play? Type 'y' to start: ").lower()
		if play == 'y':
			break
		elif play == 'n':
			clear_screen()
			print("\n" + "=" * 60)
			print("👋 Thanks for visiting the Blackjack table!")
			print("✅ Come back anytime to play!")
			print("=" * 60 + "\n")
			return
		else:
			print("❌ Please type 'y' to play or 'n' to exit.")
	
	# Main game loop
	while True:
		play_game()
		
		# Ask to play again
		while True:
			again = input("\n🔄 Play again? (y/n): ").lower()
			if again in ['y', 'n']:
				break
			print("❌ Please type 'y' or 'n'.")
		
		if again == 'n':
			clear_screen()
			print("\n" + "=" * 60)
			print("♠️ ♥️ ♦️ ♣️  THANK YOU FOR PLAYING! ♣️ ♦️ ♥️ ♠️".center(60))
			print("=" * 60)
			print("\n💡 Pro Tip: Practice makes perfect!")
			print("✅ You've mastered Ace flexibility and Blackjack logic!")
			print("\n👋 Goodbye and good luck at the tables! 🎲")
			print("=" * 60 + "\n")
			break
		else:
			clear_screen()


if __name__ == "__main__":
	main()