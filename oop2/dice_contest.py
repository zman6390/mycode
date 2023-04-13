#!/usr/bin/env python3

"""Running simulation with classes"""
from cheatdice import *

def main():
    """called at runtime"""

    swapper = Cheat_Swapper()

    loaded_dice = Cheat_Loaded_Dice()

    extra_die = Cheat_Extra_Die()

    #track scores for both players

    swapper_score = 0

    loaded_dice_score = 0

    extra_die_score = 0

    #how many games we want to run
    number_of_games = 100000

    game_number = 0

    #begin
    print("Simulation running")
    print("=================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        extra_die.roll()

        swapper.cheat()
        loaded_dice.cheat()
        extra_die.cheat()

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) == sum(extra_die.get_dice()):
            #print("Draw!")
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice() and sum(swapper.get_dice()) > sum(extra_die.get_dice()):
            #print("Dice swapper wins!")
            swapper_score += 1
            elif sum(extra_die.get_dice()) > sum(loaded_dice.get_dice()) and sum(extra_die.get_dice()) > sum(swapper.get_dice()):
            #print("Extra die wins!")
        else:
            #print("Loaded dice wins!")
            loaded_dice_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"Extra die won: {extra_die_score}")

    # determine the winner
    if swapper_score == loaded_dice_score == extra_die_score:
        print("Game was drawn")
    elif swapper_score > loaded_dice_score and swapper_score > extra_die_score:
        print("Swapper won most games")
    elif extra_die_score > loaded_dice_score and extra_die_score > swapper_score:
        print("Extra die won most games")
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()
