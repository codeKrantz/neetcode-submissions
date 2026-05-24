class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #Charconnt:List of words
        for s in strs:
            count = [0] * 26 #a to z

            for c in s:
                count[ord(c) - ord("a")] += 1 #correcly sets letter count to be a-z

            res[tuple(count)].append(s)
        return list(res.values())