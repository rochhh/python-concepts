def solution(nums):
    max_num = -9000
    min_num = 9000

    for num in nums:
        if num > max_num:
            max_num = max( num , max_num )
        if num < min_num:
            min_num = min(num , min_num)
    return f" the max is -> {max_num} and the min is -> {min_num} "

arr = [22, 14, 8, 17, 35 , 3]

print( solution(arr) )