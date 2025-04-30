class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)

        #Start at the last index
        for i in range(len(nums)-1,-1,-1):
            #Check all future index, possabilities, we want the largest one
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])

        return max(LIS)


