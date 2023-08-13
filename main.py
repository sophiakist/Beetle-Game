"""
Project One:
Main

By: Sophia Kist

Roling of dice for each player

"""
from Beetle import Beetle
from Dice import Dice

beetle_array = []
turns_list = [0 , 0, 0, 0]
winner = False
curr_player = 0

seed = input("Enter seed: ")
turn = Dice(seed)

for i in range(1, 5):
    name = input("Enter player {}'s name: ".format(i))
    beetle_array.append(Beetle(name))

while not winner:
    print("{} is going to roll the dice".format(beetle_array[curr_player].name))
    beetle_array[curr_player].handle_num(turn.dice_roll())
    winner = beetle_array[curr_player].is_complete()
    turns_list[curr_player] += 1
    curr_player = (curr_player + 1) % 4 

#move current player back to winner
curr_player -= 1

print("Game Over! {} won!".format(beetle_array[curr_player].name))
print("Turns: {}".format(turns_list[curr_player]))

    