# def solution(nums):
#     sorted_nums = []
#     res = []
#     for num in nums:
#         sorted_nums.append( abs(num) )
#     sorted_nums = sorted(sorted_nums)

#     for sn in sorted_nums:
#         res.append(sn*sn)
#     return res


def sortedSquares(nums):
    n = len(nums)
    start, end = 0, n-1
    res = [0]*n
    idx = n-1
    
    while end > -1 and idx >-1:
        if abs(nums[start]) > abs(nums[end]):
            res[idx] = nums[start] * nums[start]
            start +=1
        else:
            res[idx] = nums[end] * nums[end]
            end -= 1
        idx -= 1
    
    return res



arr = [-4,-3,0,1,10]

print(sortedSquares(arr))