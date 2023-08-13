# CPTR 142: Project #1

## Problem Overview

For this project you will create a simulation of the "Beetle" dice game.

> Beetle is a British party game in which one draws a beetle in parts. The game may be played solely with pen, paper and a die or using a commercial game set, some of which contain custom scorepads and dice and others which contain pieces which snap together to make a beetle/bug. It is sometimes called Cooties or Bugs. The game is entirely based on random die rolls, with no skill involved.
>
> ### Playing
>
> The part drawn is decided by the roll of a die. The traditional rolls are:
>
> * 6 is for the body, of which there is one.
> * 5 is for the head, of which there is one.
> * 4 is for the wings, of which there are two.
> * 3 is for a leg, of which there are six.
> * 2 is for an antenna, of which there are two.
> * 1 is for an eye, of which there are two.
>
> It is necessary to roll the correct number for the body before any other part may be drawn. To the body, one may attach the head, legs or wings, but the head must precede the antenna and eyes. The first player to draw all the requisite parts is the winner.

-- From [wikipedia.org](https://en.wikipedia.org/wiki/Beetle_(game)#/media/File:Beetle_Drive_Beetle.JPG)

Your program will simulate a game by creating a dice and some players, rolling the dice once for each player in turn, adding a body part to the beetle if appropriate, checking to see if the beetle is complete, and reporting a winner when someone has a complete beetle.

![image of beetle](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Beetle_Drive_Beetle.JPG/339px-Beetle_Drive_Beetle.JPG) 

Image by [TheRehn](https://commons.wikimedia.org/w/index.php?curid=3361932) - Own work, GFDL

## Solution Specifications

Your solution should strive to meet the standards specified below as they form the basis on which it will be graded.

1. Your program will simulate the actions by all players in an entire game, from start to finish, and report the game's outcome to the console.
1. Your program must be divided into classes and functions which perform well-defined and logical sub-tasks for the problem. You may check with your professor or TA about your choice of functions and the parameters and/or return types that they will require.
1. Define a `Dice` class and instantiate one instance to be shared by all players. Ask the user for a "seed" and use in a `Dice` constructor. Use the Python random module for setting the `random.seed()` and `random.randrange()` to simulate a dice roll to be returned.
    1. Save each class in separate files.
    1. Create a main() in the class file that tests your class, verifying that the functionality is correct.
1. Define a `Beetle` class with attributes and appropriate instance methods. Create one instance of Beetle for each of four players and ask the user for player names.
    1. Save each class in separate files.
    1. Create a main() in the class file that tests your class, verifying that the functionality is correct.
1. Create a main program to simulate the game. Give each player a turn (one roll) and move on to the next player if the game is not over. When the game ends, report which player won (by name) and how many turns it took to finish the game.
    1. Save main program in separate file.
    1. A stretch goal: Allow for a variable number of players

## Time-Saving Suggestions

The following suggestions should save you a lot of time.

* Make sure that each of your functions really encapsulates one particular well-defined task.
  If your function is more than 10-15 lines long, think carefully about if it makes sense to break it up into separate subfunctions.
* Use descriptive function and variable names.
  A function name like ``roll_dice`` is far more descriptive than ``rd`` and similarly for variables.
* For each function, include a comment that explains the input and output of the function and the task that it is responsible for completing.
* Think carefully about your code before you write it.
  It is worth programming a little slower in order to make sure that the code you write is clear, simple, and easy to read and modify.
* Start writing your functions one-by-one and test them as you write them.
  Make sure that each function behaves correctly before moving on to the next function.
  This will potentially save you a huge amount of time and frustration when debugging.
* The expected output is quite simple, just a player's name and the number of turns it took to win.
  You aren't required to report each roll or its result (though some output to a log file might be helpful for debugging).
  And you certainly aren't expected to draw a beetle!
* The use of a seed allows us to have repeatable "pseudo-random" sequences.
  If you have four players, then you should get the following results:

Seed | Player | Turns
-----|--------|------
   0 |    3   |  26  
  42 |    1   |  31  
 999 |    2   |  33

## Code Review

You should have a code review by a tutor before turning in the assignment.
See the Code Review Rubric document for expectations.
I suggest that you schedule your appointment early!
