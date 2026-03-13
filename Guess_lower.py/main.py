from os import name

from gamedata import data
import random

print("Welcome to the game!")
print("\n" + "="*60)
score = 0

account_a=random.choice(data)
account_b=random.choice(data)

print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
print(f"Compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
while account_a == account_b:
	account_b=random.choice(data)
while True:
	guess = ""
	while guess not in ["A","B"]:
		guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
		if guess not in ["A","B"]:
			print("Please enter 'A' or 'B': ")
	from gamedata import data
	import random
	
	print("Welcome to the game!")
	print("\n" + "=" * 60)
	score = 0
	
	# ===== FIX 1: Ensure distinct accounts BEFORE any display =====
	account_a = random.choice(data)
	account_b = random.choice(data)
	while account_a == account_b:  # ← MOVED BEFORE PRINTING
		account_b = random.choice(data)
	
	# ===== FIX 2: MAIN GAME LOOP (display INSIDE loop) =====
	while True:
		# DISPLAY CURRENT ACCOUNTS (inside loop!)
		print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
		print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
		
		# GET & VALIDATE GUESS (your code was perfect here ✅)
		guess = ""
		while guess not in ["A", "B"]:
			guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
			if guess not in ["A", "B"]:
				print("Please enter 'A' or 'B'")
		
		# DETERMINE CORRECT ANSWER (your code was perfect here ✅)
		if account_a['follower_count'] > account_b['follower_count']:
			correct_answer = "A"
		else:
			correct_answer = "B"
		
		# ===== FIX 3: HANDLE CORRECT GUESS PROPERLY =====
		if guess == correct_answer:
			score += 1
			
			# CLEAR SCREEN (critical for UX)
			print("\n" * 50)
			print(f"✅ You're right! Current score: {score}")
			print("=" * 60)
			
			# ROTATE ACCOUNTS (B becomes new A)
			account_a = account_b
			
			# GET NEW ACCOUNT B (ensure distinct)
			account_b = random.choice(data)
			while account_a == account_b:
				account_b = random.choice(data)
		
		# LOOP CONTINUES → new accounts display at top of loop
		else:
			# CLEAR SCREEN
			print("\n" * 50)
			print("=" * 60)
			print(f"❌ Sorry, that's wrong. Final score: {score}")
			print("=" * 60)
			break
	if account_a['follower_count']	> account_b['follower_count']:
		correct_answer ="A"
	else:
		correct_answer ="B"
		
	if guess == correct_answer:
		score += 1
		print("\n" * 50)
		print(f"You're right! current score: {score}")
		print("="*60)
	else:
		print("Wrong!")
		print(f"Your score: {score}")
		break