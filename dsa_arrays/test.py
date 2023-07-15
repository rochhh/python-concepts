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


def solution(nums,m):
    min_no = 0 
    max_no = m-1
    fin = 10000
    sorted_nums= sorted(nums)

    while max_no < len(sorted_nums):
        curr = sorted_nums[max_no] - sorted_nums[min_no]

        fin = min(fin,curr)
        min_no+=1
        max_no+=1
    return fin

nums = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50] 
m = 7

print(solution(nums,m))