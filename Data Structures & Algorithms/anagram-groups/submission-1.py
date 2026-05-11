class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            charCount = [0]*26
            for char in s:
                charCount[ord(char)-ord('a')] +=1

            hm[tuple(charCount)].append(s)

        return list(hm.values())

        