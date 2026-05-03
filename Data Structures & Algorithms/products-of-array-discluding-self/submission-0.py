class Solution:#sub-optimal
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul=1
        right_mul=1
        n=len(nums)
        left_arr=[0]*n
        right_arr=[0]*n
        for i in range(n):
            j=-i-1
            left_arr[i]=left_mul
            right_arr[j]=right_mul
            left_mul*=nums[i]
            right_mul*=nums[j]
        res=[a*b for a,b in zip(left_arr,right_arr)]
        return res
        
        