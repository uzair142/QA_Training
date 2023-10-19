import random
import time

class RPSGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.round_number = 1

    def get_user_choice(self):
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

    def get_computer_choice(self):
        print("Computer is making its choice...")
        time.sleep(2)
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        if (user == "rock" and computer == "scissors") or \
           (user == "paper" and computer == "rock") or \
           (user == "scissors" and computer == "paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def play_game(self):
        while True:
            print("\n" + "=" * 30)
            print(f"Round {self.round_number}")
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                self.user_score += 1
            elif result == "Computer wins!":
                self.computer_score += 1

            print(f"\nScore - You: {self.user_score}, Computer: {self.computer_score}")

            while True:
                play_again = input("Do you want to play another round? (yes/no): ").lower()
                if play_again in ["yes", "no"]:
                    break
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")

            if play_again != "yes":
                print("Thanks for playing!")
                break

            self.round_number += 1

if __name__ == "__main__":
    print("Welcome to Fancy Rock-Paper-Scissors Game!")
    print("=" * 40)
    game = RPSGame()
    game.play_game()
