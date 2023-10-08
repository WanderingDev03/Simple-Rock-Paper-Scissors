options = ["Rock", "Paper", "Scissors"]

def player_choice():

    while True:

        player_opt = input("Choose Rock, Paper, or Scissors: ")

        # Fix mistake in input
        if player_opt not in options:
            match player_opt:
                case "rock":
                    player_opt = "Rock"
                    break
                case "paper":
                    player_opt = "Paper"
                    break
                case "scissors":
                    player_opt = "Scissors"
                    break
                case _:
                    print("Invalid input, please try again.")
                    continue
        break
    
    print()
    print(f"You chose: {player_opt}")

    return player_opt
