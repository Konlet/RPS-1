import random

# Rock, Paper, Scissors Minus One program written by Michael M in Python for Sophia Learning - Introduction to Python course.

# Global variables

player_wins = 0
computer_wins = 0
draws = 0
hands = ["rock", "paper", "scissors"]
hand_wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# This is the primary function that will be called when the program is run. It will play a game of Rock, Paper, Scissors Minus One.
# Once the game is over, it will print the results and automatically call the play_game() function again.

def play_game():
    global player_wins, computer_wins, draws # This is a way to access the global variables without having to use the "global" keyword.
    player_first_hand = 0
    while player_first_hand not in [1, 2, 3]: # This while loop will keep asking the user for a valid hand until they enter a valid hand.
        player_first_hand = int(input("What is your first hand? 1 (Rock), 2(Paper), 3(Scissors): "))
    player_second_hand = 0
    while player_second_hand not in [1, 2, 3] and player_second_hand == player_first_hand: # This while loop will keep asking the user for a valid hand until they choose one that is different from the first hand.
        player_second_hand = int(input("What is your second hand? 1 (Rock), 2(Paper), 3(Scissors): "))
    computer_first_hand = random.choice(["rock", "paper", "scissors"])
    computer_second_hand = computer_first_hand
    while computer_second_hand == computer_first_hand: # This while loop will keep asking the computer for a valid hand until they choose one that is different from the first hand.
        computer_second_hand = random.choice(["rock", "paper", "scissors"])
    print("Player's hands: ", hands[player_first_hand-1], ", ", hands[player_second_hand-1]) # This will print the hands of the player and computer.
    print("Computer's hands: ", computer_first_hand, ", ", computer_second_hand)
    player_removed_hand = 0
    while player_removed_hand not in [1, 2]: # This while loop will keep asking the user for a valid hand to remove until they enter a valid hand.
        player_removed_hand = int(input(f"Which hand would you like to remove? 1 ({hands[player_first_hand-1]}), 2 ({hands[player_second_hand-1]}): "))
    player_remaining_hand = player_first_hand if player_first_hand != player_second_hand else player_second_hand # This will determine which of the player's hands is the remaining hand.
    computer_removed_hand = random.choice([computer_first_hand, computer_second_hand])
    computer_remaining_hand = computer_first_hand if computer_first_hand != computer_removed_hand else computer_second_hand # This will determine which of the computer's hands is the remaining hand.
    print("Player's remaining hand: ", hands[player_remaining_hand-1]) # This will print the remaining hand of the player and computer.
    print("Computer's remaining hand: ", computer_remaining_hand)

    # This if statement will determine which hand wins and will print the result.
    if hand_wins[hands[player_first_hand-1]] == computer_remaining_hand:
        print("Player wins!")
        player_wins += 1
    elif hand_wins[computer_remaining_hand] == hands[player_first_hand-1]:
        print("Computer wins!")
        computer_wins += 1
    else:
        print("It's a tie!")
        draws += 1
    
    print("Player wins: ", player_wins, ", Computer wins: ", computer_wins, ", Draws: ", draws) # This will print the results of the game.
    # At this point, the game is over and the play_game() function will be called again.


def main():
    while True:
        play_game()

if __name__ == "__main__":
    main()
