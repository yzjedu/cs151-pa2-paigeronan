# Code goes here and DO NOT FORGET INTRO COMMENTS
from random import randint
from random import randint
import random
def play():
    sticks = int(input("How many sticks in total for the game(10-100):"))
    while sticks < 10 or sticks > 100:
        print("Must choose 10-100")
        sticks = int(input("How many sticks in total for the game(10-100):"))
    player = 1
    SENTINEL = 0
    while sticks > SENTINEL:
        print("Player", player, "it is your turn")
        print("There are", sticks, "sticks")

        if player == 3:
            computer_sticks = random.randint(1, 3)
            if sticks < 3:
                computer_sticks = random.randint(1, 2)
            elif sticks < 2:
                computer_sticks = 1
            sticks = sticks - computer_sticks
            print("Player 3 takes", computer_sticks, "sticks")
            player = 1
        elif player == 2 or player == 1:
            take_sticks = int(input("How many sticks to you want to take?"))
            while take_sticks < 1 or take_sticks > 3:
                print("Must choose 1-3")
                take_sticks = int(input("How many sticks to you want to take?"))
            sticks = sticks - take_sticks

            player = player + 1
            if player > 3:
                player = 1
    player = player - 1
    if player == 0:
        player = 3
    print("Player", player, "lost.")
    loses = 0
    if sticks == 0:
        player_lose = player
        loses += 1
        print(f"Player {player} has {loses} loses")


play()
play_again = input("Would you like to play again? (y/n) ")
while play_again == "y":
    play()
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "n":
        print("Thanks for playing!")
    else:
        print("Please choose either 'y' or 'n'")