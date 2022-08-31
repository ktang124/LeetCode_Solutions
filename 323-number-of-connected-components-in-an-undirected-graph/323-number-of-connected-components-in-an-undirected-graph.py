class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for fr, to in edges:
            graph[fr].append(to)
            graph[to].append(fr)
        
        numConnect = 0
        visited = [0] * n
        def dfs(i, graph, visited):
            if visited[i] == 0:
                visited[i] = -1
                for component in graph[i]:
                    dfs(component, graph, visited)
                visited[i] = 1
        for i in range(n):
            if visited[i] == 0:
                numConnect += 1
                dfs(i, graph, visited)
        return numConnect