import random
import time

def get_user_choice():
    while True:
        print("\nChoose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter the number (1/2/3): ")
        if user_choice in ["1", "2", "3"]:
            return ["rock", "paper", "scissors"][int(user_choice) - 1]
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def get_computer_choice():
    print("Computer is making its choice...")
    time.sleep(2)
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print("\n" + "="*30)
        print(f"Round {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        while True:
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

        if play_again != "yes":
            print("Thanks for playing!")
            break

        round_number += 1

if __name__ == "__main__":
    print("Welcome to Fancy Rock-Paper-Scissors Game!")
    print("="*40)
    play_game()
