class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        n = len(nums)

        if n == 1:
            return prefix + 1

        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            prefix += nums[i]
            i += 1

        present = set(nums)
        while prefix in present:
            prefix += 1

        return prefix