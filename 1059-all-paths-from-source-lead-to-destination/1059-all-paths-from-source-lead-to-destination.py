class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        #build graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            
            graph[edge[0]].append(edge[1])
            
       
            
        colors = [0] * n
        #only empty edge can be the destination
        def dfs(graph, source, destination, colors):
            if colors[source] != 0:
                return colors[source] == 2
            #cycle detection
            if len(graph[source]) == 0:
                return source == destination
            #visiting
            colors[source] = 1
            for adj in graph[source]:
                if not dfs(graph, adj, destination, colors):
                    return False
                
            colors[source] = 2
            return True
            
                
        return dfs(graph, source, destination, colors)
        