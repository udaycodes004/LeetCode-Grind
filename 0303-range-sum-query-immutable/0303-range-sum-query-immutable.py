class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pfx = [0] * n

        self.pfx[0] = nums[0]
        for i in range(1, n):
            self.pfx[i] = self.pfx[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pfx[right]
        return self.pfx[right] - self.pfx[left-1]