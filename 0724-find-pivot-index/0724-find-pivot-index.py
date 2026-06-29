class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        leftsum=0
        total=sum(nums)
        for i in range(n):
            rightsum=total-leftsum-nums[i]
            if (rightsum==leftsum):
                return i
            leftsum+=nums[i]
        return -1

        