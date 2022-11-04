class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            anagramGroups[key].append(s)
        return anagramGroups.values()
            