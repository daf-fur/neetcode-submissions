class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create an empty set
        emptySet = set()

        # check for whether the element is in the set, if not add
        for n in nums:
            if (n in emptySet):
                return True
            
            emptySet.add(n)

        return False
