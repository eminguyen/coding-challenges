# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) == 2):
            return [nums, nums[::-1]]
        if(len(nums) <= 1):
            return [nums]
        permutations = []
        for index, number in enumerate(nums):
            list_copy = nums.copy()
            list_copy.pop(index)
            for array in self.permute(list_copy):
                array.insert(0, number)
                permutations.append(array)
        return permutations
