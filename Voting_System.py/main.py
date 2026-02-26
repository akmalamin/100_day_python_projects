"""
Voting System
Anonymous voting system that tracks votes for candidates and announces results.
"""


def main():
	# Phase 1: Setup
	candidates = ["Alice", "Bob", "Charlie", "David"]

	# Initialize votes dictionary with all candidates at 0
	votes = {candidate: 0 for candidate in candidates}

	print("=" * 50)
	print("🗳️  WELCOME TO THE VOTING SYSTEM")
	print("=" * 50)
	print(f" Candidates: {', '.join(candidates)}\n")

	# Phase 2: Voting Loop
	while True:
		# Clear screen between voters (simple method)
		print("\n" * 3)

		# Get and normalize vote
		vote_input = input("Who are you voting for? ").strip().title()

		# Validate and record vote
		if vote_input in candidates:
			votes[vote_input] += 1  # ✅ CRITICAL FIX: Only increment VOTED candidate
			print(f"✓ Vote recorded for {vote_input}!")
		else:
			print(f"❌ Invalid candidate! Choose from: {', '.join(candidates)}")
			continue  # Reprompt same voter

		# Ask for more voters
		more = input("\nMore voters? (y/n): ").strip().lower()
		if more in ['n', 'no']:
			break
		elif more not in ['y', 'yes']:
			print("⚠️  Invalid response. Assuming 'yes' for next voter.")

	# Phase 3: Calculate Results
	total = sum(votes.values())

	# Find winner(s) BEFORE display loop
	if total > 0:
		max_votes = max(votes.values())  # ✅ Define max_votes FIRST
		winners = [name for name, count in votes.items() if count == max_votes]  # ✅ Use .items()
	else:
		winners = []

	# Phase 4: Display Results
	print("\n" + "=" * 50)
	print("📊 ELECTION RESULTS")
	print("=" * 50)

	if total == 0:
		print("⚠️  No votes were cast!")
	else:
		# Display each candidate's results
		for candidate in candidates:
			count = votes[candidate]
			percentage = (count / total) * 100  # ✅ Calculate PER candidate
			print(f"{candidate:<12} {count:>3} votes ({percentage:>5.1f}%)")

		print("-" * 50)
		print(f"TOTAL VOTES: {total}")

		# Announce winner(s)
		print("\n" + "=" * 50)
		if len(winners) == 1:
			print(f"🎉 WINNER: {winners[0]} with {votes[winners[0]]} votes!")
		elif len(winners) > 1:
			winner_list = " and ".join(winners)
			print(f"🎉 TIE! Winners: {winner_list}")
			print(f"    Each received {max_votes} votes")
		else:
			print("⚠️  No winner determined")

	print("=" * 50)
	print("🙏 Thank you for voting!")
	print("=" * 50)


if __name__ == "__main__":
	main()