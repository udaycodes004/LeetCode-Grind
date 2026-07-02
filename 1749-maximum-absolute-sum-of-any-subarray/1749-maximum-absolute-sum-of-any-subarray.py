class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mxx = 0
        mnn = 0
        sm = 0

        for num in nums:
            sm += num
            mxx = max(mxx, sm)
            mnn = min(mnn, sm)

        return mxx-mnn