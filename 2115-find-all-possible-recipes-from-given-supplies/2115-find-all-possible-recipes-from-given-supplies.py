class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
       
        visited = set()
        degrees = defaultdict(lambda: 0)
        graph = defaultdict(lambda: set())
        #this asks, what do we need to make the food?
        #base ingredients have degree 0, which means they can be added to the queue
        #as we visit these ingredients, we can see if we need any more ingredients to build the other foods
        for idx, ingredientList in enumerate(ingredients):
            food = recipes[idx]
            for ingredient in ingredientList:
                graph[ingredient].add(food)
                degrees[food] += 1
        
        queue = supplies
        while queue:
            cur = queue.pop(0)
            for ingredient in graph[cur]:
                degrees[ingredient] -= 1
                if degrees[ingredient] == 0:
                    queue.append(ingredient)
                    
            visited.add(cur)
            
        return list(visited.intersection(recipes))
            
        
        