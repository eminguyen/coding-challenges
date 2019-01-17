# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        memo = {}
        memo[0] = 0
        memo[1] = 1
        for i in range(2, N+1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[N]
