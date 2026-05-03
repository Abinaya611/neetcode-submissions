class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l,r=0,0
        n=min(len(word1),len(word2))
        res=""

        while l<n and r<n:
            res+=word1[l]
            res+=word2[r]
            l+=1
            r+=1

        res+=word1[l:]
        res+=word2[r:]

        return res



        