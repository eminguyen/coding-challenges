# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safe_nodes = []
        for node in range(len(graph)):
            if(self.isSafeNode(graph, node)):
                safe_nodes.append(node)
        return safe_nodes
    
    def isSafeNode(self, graph, node):
        if graph[node] == []:
            return True
        if graph[node] == [-1] :
            return False
        if graph[node] == [-2] :
            return True
        adjacency = graph[node].copy()
        graph[node] = [-1] 
        for n in adjacency:
            if not self.isSafeNode(graph, n):
                return False        
        else:
            graph[node] = [-2]
        return True
