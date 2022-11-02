class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        levels = 0
        queue = [start]
        visited = set()
        while queue:
            size = len(queue)
            while size:
                size -=1
                poll = queue.pop(0)
                visited.add(poll)
                if poll == end:
                    return levels
                for word in bank:
                    diff = 0
                    if word not in visited:
                        for i, c in enumerate(poll):
                            if word[i] != c:
                                diff += 1
                        if diff == 1:
                            queue.append(word)
                        
            levels += 1
        return -1