"""Rock, paper, scissors!

Rock, paper, scissors made on Python.
"""

import random


def computer_choice():
    """Gets a random option for the computer to use."""
    computer = random.choice(options)
    return computer


def user_choice():
    """Gets the option the player will use."""
    user = str(input("Select what you want to play this round: Rock, paper, scissors.\n"))
    user = user.lower()
    if user in options:
        return user
    else:
        raise Exception("Your choice is not valid. Check for typos and try again.")


def run_game():
    """Starts and handles the game from start to finish."""
    rounds = 3
    user_win = 0
    computer_win = 0

    print("*" * 15)
    print("The game will start now.")
    print("*" * 15)
    
    while True:
        computer = computer_choice()
        user = user_choice()
        print(f"{user} vs {computer}, ")

        if user == computer:
            # It's a tie
            rounds -= 1
            print(f"""
            Tie!
            You have both picked {user}
            {rounds} remaining.
            """)

        elif (user == "scissors" and computer == "paper") or \
             (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock"):
            # User wins this round
            rounds -= 1
            user_win += 1
            print(f"""
            You have won this round!
            {user} beats {computer}!
            {rounds} remaining.
            """)

        else:
            # Computer wins this round
            rounds -= 1
            computer_win += 1
            print(f"""
            You have lost this round.
            {computer} beats {user}!
            {rounds} remaining.
            """)

        if rounds <= 0:
            # Determine the overall winner
            if user_win == computer_win:
                print("It's a tie, you ended the game with the same amount of points.")
            elif computer_win > user_win:
                print(f"Match ended. The winner is the computer with {computer_win} points.")
            else:
                print(f"Match ended. You are the winner with {user_win} points!")
            break


if __name__ == "__main__":
    # Global choice options.
    options = ("rock", "paper", "scissors")
    run_game()
