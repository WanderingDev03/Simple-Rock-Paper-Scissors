from computer import computer_choice
from player import player_choice

options = ["Rock", "Paper", "Scissors"]

def winning_case(player, computer):
    if player == "Rock" and computer == "Scissors":
        return True
    elif player == "Scissors" and computer == "Paper":
        return True
    elif player == "Paper" and computer == "Rock":
        return True
    else:
        return False

def main():

    player = player_choice()
    computer = computer_choice()
    print()
    if player == computer:
        print("It's a tie!")
    elif winning_case(player, computer):
        print(f"You win! {player} beats {computer}")
    else:
        print(f"You lose! {computer} beats {player}")

if __name__ == "__main__":
    main()
