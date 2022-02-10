#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

# number 1
class AIPlayer(Player):
    """an AIPlayer for connect four"""


# Function 2
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead



# Function 3
    def __repr__(self):
        """returns a string representing an AIplayer object. It also indicates which checker it will use"""
        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')')



# Function 4
    def max_score_column(self, scores):
        """ returns the index of the columb with the maximum score"""
        max_score = []
       
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_score += [i]

        if self.tiebreak == 'LEFT':
            return max_score[0]

        if self.tiebreak == 'RIGHT':
            return max_score[-1]

        if self.tiebreak == 'RANDOM':
            return random.choice(max_score)

# Function 4
    def scores_for(self, b):
        """takes a board and determines the called AIplayer's score"""
        # list long enough for each column 
        scores = [0] * len(range(b.width)) 
        for col in range(b.width):

            #If the current column is full, use a score of -1 for it
            if b.can_add_to(col) == False:
                scores[col] = -1

            # if b is already a win for the called AIPlayer, use a score of 100 for the current column.
            elif b.is_win_for(self.checker):
                scores[col] = 100

            #b is already a win for the player’s opponent, use a score of 0 for the current column.
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0

            #f the player has a lookahead of 0, use a score of 50 for the column
            elif self.lookahead == 0:
                scores[col] = 50

            # Otherwise, we need to look ahead
            else:
                b.add_checker(self.checker, col)
                player_two = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                score_two = player_two.scores_for(b)
                if max(score_two) == 0:
                    scores[col] = 100
                elif max(score_two) == 100:
                    scores[col] = 0 
                elif max(score_two) == 50:
                    scores[col] = 50
            
                b.remove_checker(col)
        return scores

        # Function 5
    def next_move(self, board):
        """returns the called AIPlayer's jugdment of its best possible move"""
        self.num_moves +=1
        scores = self.scores_for(board)
        return self.max_score_column(scores)