class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptyDict = {} # value, index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in emptyDict:
                return [emptyDict[difference], i]
            emptyDict[n] = i
        return 