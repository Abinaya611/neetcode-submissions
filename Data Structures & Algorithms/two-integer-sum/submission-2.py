class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        n=len(nums)
        hashMap={}
        for i in range(n):
            diff=target-nums[i]
            if diff in hashMap:
                res.extend([hashMap[diff],i])
                return res
            hashMap[nums[i]] = i

        return res
            
        
        