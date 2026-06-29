class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        zero=0
        n=len(nums)
        for r in range(n):
            if nums[r]==0:
                zero+=1
            if zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
        return r-left+1
        