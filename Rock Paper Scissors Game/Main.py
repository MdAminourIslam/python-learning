import random
option = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(option)

def get_user_choice():
    choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock, Paper, Scissors with Score Tracking!\n")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round! ✅")
            user_score += 1
        else:
            print("Result: Computer wins this round! ❌")
            computer_score += 1

        print(f"\nCurrent Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\n🏁 Final Score:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing!")
            break

        round_number += 1

# Start the game
play()
