class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        pfxsum=0
        freq={0:1}
        for num in nums:
            pfxsum+=num
            rem=pfxsum%k
            if rem in freq:
                count+=freq[rem]
            freq[rem]=freq.get(rem,0)+1
        return count
        