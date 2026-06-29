class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pfx=[0]*n
        for i in range(n):
            pfx[i]=pfx[i-1]+nums[i]

        freq={}
        count=0
        for j in range(n):
            if pfx[j]==k:
                count+=1
            diff=pfx[j]-k
            if diff in freq:
                count+=freq[diff]
            
            freq[pfx[j]]=freq.get(pfx[j],0)+1
        print(pfx)
        print(freq)
        return count



        