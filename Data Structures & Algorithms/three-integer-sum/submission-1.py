class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result=set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 tmp=(nums[i],nums[j],nums[k])
        #                 result.add(tmp)
        # return [ list(i) for i in result]

        # res=set()
        # third=0
        # for i in range(len(nums)):
        #     hashh=set()
        #     for j in range(i+1,len(nums)):
        #         third=-(nums[i]+nums[j])
        #         if third  in hashh :
        #             tmp=tuple(sorted([nums[i],nums[j],third]))
        #             res.add(tmp)
        #         hashh.add(nums[j])
        # return [list(i) for i in res]

        res=set()
        nums.sort()
        summ=0

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if summ<0:
                    j+=1
                elif summ>0:
                    k-=1
                else:
                    tmp=[nums[i],nums[j],nums[k]]
                    res.add(tuple(tmp))
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return [list(i) for i in res]
                    
                





        

        