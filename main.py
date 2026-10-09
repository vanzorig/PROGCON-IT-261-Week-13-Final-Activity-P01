import random


def get_player_choice():
    """Ask the player to choose Rock, Paper, or Scissors."""
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choices = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors",
    }

    choice = input("Enter your choice (1-3 or name): ").strip().lower()

    while choice not in choices and choice not in ("rock", "paper", "scissors"):
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        choice = input("Enter your choice (1-3 or name): ").strip().lower()

    if choice in choices:
        return choices[choice]

    return choice.capitalize()


def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["Rock", "Paper", "Scissors"])


def determine_winner(user_input, computer_guess):
    """Display the result of the round."""
    if user_input == computer_guess:
        print("It's a draw!")
    elif (
        (user_input == "Rock" and computer_guess == "Scissors")
        or (user_input == "Paper" and computer_guess == "Rock")
        or (user_input == "Scissors" and computer_guess == "Paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")


def play_again():
    """Ask whether the player wants another round."""
    answer = input("\nDo you want to play again? (yes/no): ").strip().lower()

    while answer not in ("yes", "no"):
        answer = input("Please enter yes or no: ").strip().lower()

    return answer == "yes"


def main():
    """Run the Rock, Paper, Scissors game."""
    print("=== ROCK, PAPER, SCISSORS ===")

    while True:
        user_input = get_player_choice()
        computer_guess = get_computer_choice()

        print("\nYour choice:", user_input)
        print("Computer's choice:", computer_guess)

        determine_winner(user_input, computer_guess)

        if not play_again():
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()
