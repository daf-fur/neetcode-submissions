class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val, index

        for i, n in enumerate(nums): # enumerate yields index and value
            diff = target - n # the value n needs to complete the target
            if diff in prevMap:
                return [prevMap[diff], i] # return partner's index, then own index
            prevMap[n] = i #store number n with index i