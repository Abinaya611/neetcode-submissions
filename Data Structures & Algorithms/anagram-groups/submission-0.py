class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        res=[]
        for s in strs:
            sorting=''.join(sorted(s))
            hm.setdefault(sorting,[]).append(s)

        for k,v in hm.items():
            res.append(v)
        return res
        