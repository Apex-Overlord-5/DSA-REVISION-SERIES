class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right]==0:
                nums.append(0)
                nums.remove(0)

# THE ABOVE APPROACH IS A BAD APPROACH