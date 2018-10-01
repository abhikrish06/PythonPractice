class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        trgt = len(graph) - 1

        def dfs(node, prev_node):
            if node == trgt:
                res.append(prev_node + [node])
                return
            for val in graph[node]:
                dfs(val, prev_node + [node])

        res = []
        dfs(0, [])
        return res