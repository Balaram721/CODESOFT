import random

def rock_paper_scissors():
    print("\n--- Welcome to Rock, Paper, Scissors Game !! ---")
    user_score = 0
    computer_score = 0

    while True:
        print(f"\nScores: You - {user_score}, Computer - {computer_score}")
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user_choice = input("Enter your choice: ")
        if user_choice == '4':
            print("\nThank you for playing! Final scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

        choices = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}
        if user_choice not in choices:
            print("Invalid choice! Please select again.")
            continue

        user_move = choices[user_choice]
        computer_move = random.choice(list(choices.values()))

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == 'Rock' and computer_move == 'Scissors') or \
             (user_move == 'Paper' and computer_move == 'Rock') or \
             (user_move == 'Scissors' and computer_move == 'Paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThank you for playing! Final scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

rock_paper_scissors()