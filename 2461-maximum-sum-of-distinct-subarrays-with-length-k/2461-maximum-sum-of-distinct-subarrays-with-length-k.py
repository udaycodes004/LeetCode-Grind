class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = {}
        window_sum = 0
        max_sum = 0
        l = 0

        for r in range(len(nums)):
            window_sum += nums[r]
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            if (r - l + 1) > k:
                window_sum -= nums[l]
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            if (r - l + 1) == k and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum