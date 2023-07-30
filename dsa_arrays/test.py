'''
Failed -

missingNo
moveZeroes
singleNumber 
valid palindrome
abs sorted integers (abs_sorted_integer_squared.py) done by me in 0(nlogn) can be done in o(n)

rotated sorted array search 

Successful - 

twosum (√)
contains Duplicate 
rev arr 
anagram 
max , min no in an array 
chocolate distribution 
maximum subarray ( !!!! got wrong after prac again  !!! )
stock ~( little gray )
nums disappearing in an array ~( little gray )
first last elem in a sorted array

'''


def soln(nums):
    i = 0
    j = 1
    curr_sum = nums[i]
    max_sum = -1000000

    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 0 :
        return 

    while j < len(nums):

        curr_sum = curr_sum + nums[j]
        max_sum = max(max_sum,curr_sum)

        if curr_sum < 0:
            curr_sum = 0
            i+=1

        j += 1

    return max_sum


nums= [-2,1,-3,4,-1,2,1,-5,4]

print(soln(nums))
