'''
To do -
twosum
missingNo

Successful - 
contains Duplicate 
rev arr 
anagram 
max , min no in an array 

'''


def solution(nums):

    ''' max min in an array '''
    
    sorted_arr = sorted(nums)
    min_no = 0
    max_no = len(sorted_arr)-1

    return f" min is {sorted_arr[min_no]} and the max is {sorted_arr[max_no]}  "


nums = [4,-3,978,1,99,12]     


print(solution(nums))