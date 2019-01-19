# https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        
        # Sort workers in order
        worker = sorted(worker)
        worker_pair = []
        
        # Sort the difficulty into list with tuples
        for index, level in enumerate(difficulty):
            money = profit[index]
            worker_pair.append((level, money))
            
        worker_pair = sorted(worker_pair)
        
        curr_profit = 0
        curr_index = 0
        max_profit = 0

        # Iterate through each person and determine most profit they can make
        for person in worker:
            while(curr_index < len(worker_pair) and person >= worker_pair[curr_index][0]):
                max_profit = max(max_profit, worker_pair[curr_index][1])
                curr_index += 1
            curr_profit += max_profit
            
        return curr_profit
