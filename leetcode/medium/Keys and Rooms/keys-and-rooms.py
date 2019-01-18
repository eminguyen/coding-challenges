# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        count = len(rooms)
        stack = [0]
        while(len(stack) > 0):
            index = stack.pop()
            if(rooms[index] != [-1]):
                count -= 1
            for key in set(rooms[index]):
                if(key > 0):
                    stack.append(key)
            rooms[index] = [-1]
        return count == 0
