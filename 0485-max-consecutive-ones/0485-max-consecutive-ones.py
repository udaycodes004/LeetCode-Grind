class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones=0
        mx=0
        for i in range(len(nums)):
            if nums[i]==1:
                ones+=1
                mx=max(mx,ones)
            else:
                ones=0
        return mx
        