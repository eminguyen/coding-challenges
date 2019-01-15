# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) <= 1):
            return [nums]
        if(len(nums) == 2):
            if(nums == nums[::-1]):
                return [nums]
            return [nums, nums[::-1]]
        permutations = []
        alreadyPermuted = {}
        for index, number in enumerate(nums):
            if number in alreadyPermuted:
                continue
            alreadyPermuted[number] = 1
            list_copy = nums.copy()
            list_copy.pop(index)
            for array in self.permuteUnique(list_copy):
                array.insert(0, number)
                permutations.append(array)
        return permutations
            
