class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #make a graph
        #all the relationships you can have
        graph = defaultdict(set)
        #all the relationships you cannot have
        antiGraph = defaultdict(set)
        for eq in equations:
            sign = eq[1:3]
            a = eq[0]
            b = eq[3]
            if sign == '==':
                graph[a].add(b)
                graph[b].add(a)
            else:
                if a == b:
                    return False
                antiGraph[a].add(b)
                antiGraph[b].add(a)
                
        
        for key in graph:
            bSet = antiGraph[key]
            stack = [key]
            visited = set()
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    for n in graph[cur]:
                        if n in bSet:
                            return False
                        stack.append(n)
                visited.add(cur)
        return True
                
                
        