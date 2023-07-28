'''
Failed -

twosum
missingNo
moveZeroes
singleNumber 
valid palindrome
abs sorted integers (abs_sorted_integer_squared.py) done by me in 0(nlogn) can be done in o(n)
rotated sorted array search 
first last elem in a sorted array 


Successful - 

contains Duplicate 
rev arr 
anagram 
max , min no in an array 
chocolate distribution 
maximum subarray 
stock ~( little gray )
nums disappearing in an array ~( little gray )

'''


def soln(nums):

    count = 0
    i = 0
    j = len(nums)-1

    while i < j:
        res = 0
        if nums[i] == nums[j]:
            res = res + nums[i]
            i+=1        
        if nums[i] != nums[j]:        
            count = count + nums[i] + res

            j-=1


        


    return count


nums = [4,3,2,7,8,2,3,1]
print(soln(nums))