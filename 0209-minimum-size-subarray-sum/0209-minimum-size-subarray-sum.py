class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        add=0
        l=0
        for r in range(len(nums)):
            add+=nums[r]

            while(add>=target):
                if r-l+1<ans:
                    ans=r-l+1
                add-=nums[l]
                l+=1
        if ans!=float('inf'):
            return ans
        else:
            return 0
            


