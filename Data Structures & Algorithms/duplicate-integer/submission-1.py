class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n=len(nums)
        # l,r=0,1
        # nums.sort()
        # while r<n:
        #     if nums[l]==nums[r]:
        #         return True
        #     l,r=l+1,r+1
        
        
        # return False

        hashSet=set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)

        return False
    


            
        