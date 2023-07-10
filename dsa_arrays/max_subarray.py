# Do again !


def solution(nums):
    curr_max = 0
    fin = float('-inf')

    for num in nums:
        curr_max = curr_max + num

        if curr_max > fin:
            fin = curr_max

        if curr_max < 0:
            curr_max = 0
    return fin 


arr = [-2,1,-3,4,-1,2,1,-5,4]

print(solution(arr))