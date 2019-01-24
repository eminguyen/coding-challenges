class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # Iterate through the board and mark each value
        for row in range(len(board)):
            for column in range(len(board[0])):
                num_neighbors = self.getNumNeighbors(board, row, column)
                if(board[row][column] == 1):
                    if(num_neighbors < 2 or num_neighbors > 3):
                        board[row][column] = 2
                else:
                    if(num_neighbors == 3):
                        board[row][column] = -1
            
        # Iterate through the board again and update each value
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(board[r][c] == 2):
                    board[r][c] = 0
                elif(board[r][c] == -1):
                    board[r][c] = 1
                    
    def getNumNeighbors(self, board, x, y):
        neighbors = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if(i == x and j == y):
                    continue
                if(i >= 0 and i < len(board) and j >= 0 and j < len(board[0])):
                    if(board[i][j] > 0):
                        neighbors += 1
        return neighbors
