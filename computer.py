from random import choice

options = ["Rock", "Paper", "Scissors"]

def computer_choice():

    res = choice(options)
    print(f"Computer choice is: {res}")
    return res
