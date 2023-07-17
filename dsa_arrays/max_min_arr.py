def solution(nums):
    max_num = -9000
    min_num = 9000

    for num in nums:
        if num > max_num:
            max_num = max( num , max_num )
        if num < min_num:
            min_num = min(num , min_num)
    return f" the max is -> {max_num} and the min is -> {min_num} "

arr = [4,-3,978,1,99,12]

print( solution(arr) )










'''

def solution(nums):

    also works !!
    
    sorted_arr = sorted(nums)
    min_no = 0
    max_no = len(sorted_arr)-1

    return f" min is {sorted_arr[min_no]} and the max is {sorted_arr[max_no]}  "


'''