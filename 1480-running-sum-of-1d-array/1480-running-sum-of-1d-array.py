class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pfx=[0]*n

        for i in range(n):
            pfx[i]=pfx[i-1]+nums[i]
        return pfx
        