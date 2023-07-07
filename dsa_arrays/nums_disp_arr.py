def solution(nums):
    set_nums = set(nums)
    missing = []

    for i in range( 1, len(nums)+1 ):
        if i not in set_nums:
            missing.append(i)
    return missing

arr = [4,3,2,7,8,2,3,1]

print(solution(arr))