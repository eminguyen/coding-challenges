"""
Problem:

Initially, there is a Robot at position (0, 0). 
Given a sequence of its moves, judge if this robot makes a circle, 
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for i in range(len(moves)):
            if(moves[i] == "L"):
                x += 1
            elif(moves[i] == "R"):
                x -= 1
            elif(moves[i] == "U"):
                y += 1
            else:
                y -= 1
        if x == 0 and y == 0:
            return True
        return False
