class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # for i in nums:
        #     if nums.count(i) > 1:
        #         return True      
        #     return False

        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False 