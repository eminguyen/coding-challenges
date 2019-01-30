# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(0, len(flowerbed)):
            if((i < 1 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i > len(flowerbed)-2 or flowerbed[i+1] == 0)):
                count += 1
                flowerbed[i] = 1
        return count >= n
