class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right]==0:
                nums.append(0)
                nums.remove(0)

# THE ABOVE APPROACH IS A BAD APPROACH

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non0 = 0
        for zero in range(len(nums)):
            if nums[zero]!=0:
                nums[zero] , nums[non0] = nums[non0], nums[zero]
                non0+=1

        return nums
        
            