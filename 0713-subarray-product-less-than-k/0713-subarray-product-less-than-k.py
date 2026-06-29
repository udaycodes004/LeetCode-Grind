class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod=1
        left=0
        ans=0
        for r in range(len(nums)):
            prod*=nums[r]
            while prod>=k:
                prod//=nums[left]
                left+=1
            ans+=r-left+1
        return ans

        
            
        