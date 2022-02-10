#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    """  TODO """
    # Function 1
    def __init__(self, checker):
        """constructs a new player object by initializing a checker and number of moves"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0


    # Function 2
    def __repr__(self):
        """returns a string representing a player object and what checker it is using"""
        if self.checker == 'O':
            return 'Player O'
        else:
            return 'Player X'


    # Function 3
    def opponent_checker(self):
        """returns a one character string representing the checker of the opponent"""
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'

    # Function 4
    def next_move(self, b):
        """ Get a next move for this player that is valid for the board b.""" 
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            # if valid column index, return that integer
            # else, print 'Try again!' and keep looping
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')