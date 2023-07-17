'''
To do -
twosum
missingNo
moveZeroes
singleNumber 

Successful - 
contains Duplicate 
rev arr 
anagram 
max , min no in an array 
chocolate distribution 


'''


def solution(nums):
    i = 0
    j = 1
    fin = -100000
    while j < len(nums):
        curr = nums[i] + nums[j]
        fin = max(curr,fin)

        if curr < 0:
            curr = 0
            i+=1

        if nums[i] < 0:
            i = j
                 
        j+=1
    return fin 
nums = [5,4,-1,7,8]

print(solution(nums))