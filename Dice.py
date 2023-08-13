"""
Project One:
Dice

By: Sophia Kist
"""
import random

class Dice:
    def __init__(self, seed):
        self.num = 0
        random.seed(seed)
    def dice_roll(self):
        num = random.randrange(1,7)
        self.num = num
        return num
def main():
    playing = Dice(19)
    print(playing.dice_roll())
    print(playing.dice_roll())
    print(playing.dice_roll())
    print(playing.dice_roll())
    print(playing.dice_roll())
    print(playing.dice_roll())
    print(playing.dice_roll())
    print(playing.num)
    print(playing.dice_roll())
