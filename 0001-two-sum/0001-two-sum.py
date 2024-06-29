class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wlen = len(nums)
        for i in range(wlen):
            for j in range(i+1, wlen):
                if nums[i]+nums[j] == target:
                    return [i,j]
                else:
                    continue

        return
    