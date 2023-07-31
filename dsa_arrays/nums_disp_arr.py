def solution(nums):
    # set_nums = set(nums)
    missing = []

    for i in range( 1, len(nums)+1 ):
        if i not in nums:
            missing.append(i)
    return missing

arr = [4,3,2,7,8,2,3,1]

print(solution(arr))


def opti(nums):

    for num in nums:
        index = abs(num) - 1
        nums[index] = -1*abs(nums[index])

    res = []

    for i , n in enumerate(nums):

        if n > 0 :

            res.append(i+1)
        
    return res



'''

opti but simpler to understand :===>

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res



'''