class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        for s in strs: 
            anagramGroups[str(sorted(s))].append(s)
        return anagramGroups.values()
            