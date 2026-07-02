class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
    
        mxx=float("-inf")
        add=0
        for i in range(len(nums)):

            add+=nums[i]
            if add>mxx:
                mxx=add
            if add<0:
                add=0
        return mxx
        
        