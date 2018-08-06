"""
Problem:

At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.
"""

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
            elif b == 20:
                if tens < 1:
                    if fives < 3:
                        return False
                    fives -= 3
                else:
                    if fives < 1:
                        return False
                    fives -=1
                    tens -= 1
        return True
