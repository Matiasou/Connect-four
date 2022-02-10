#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

# Function 1
def process_move(p, b):
    """it will perform all the steps involved in processing a single move by a player on the board"""
    
    #a
    print(str(p) + "'s turn")
    
    #b
    next_move = p.next_move(b)

    #c
    b.add_checker(p.checker, next_move)
    
    #d
    print()
    print(b)

    #e
    if b.is_win_for(p.checker):
        print(str(p)+ ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    if b.is_full():
        print("It's a Tie")
        return True
    #f
    else:
        return False

# Function 2

class RandomPlayer(Player): # <-- inheritance from Player like in coursepack
    
    def next_move(self, b):
        column = []
        for i in range(b.width):
            for col in range(b.width):
                if self.can_add_to(col):
                    col[i]
        return random.choice(col)

