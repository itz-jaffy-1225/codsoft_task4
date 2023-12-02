import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock, Paper, Scissors Game ---")

    # User choice input
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            break
        else:
            print("Invalid choice. Please enter rock, paper, or scissors")

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    print(result)
    print(f"\nScore - You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
