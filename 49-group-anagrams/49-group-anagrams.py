class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(lambda:[])
        for string in strs:
            k = sorted(string)
            key = str(k)
            anagramGroups[key].append(string)
            
        res = []
        for key in anagramGroups:
            res.append(anagramGroups[key])
            
        return res
            