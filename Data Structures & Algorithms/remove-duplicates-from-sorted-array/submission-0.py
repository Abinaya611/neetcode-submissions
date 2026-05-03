class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index=0
        n=len(nums)
        l=0
        r=l+1
        while(r<n):
            
            if nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
                
            
            
            r+=1

        return l+1

            
                
        

        