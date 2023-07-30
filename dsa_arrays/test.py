'''
Failed -

missingNo
moveZeroes
singleNumber 
valid palindrome
abs sorted integers (abs_sorted_integer_squared.py) done by me in 0(nlogn) can be done in o(n)
rotated sorted array search 

Successful - 

twosum
contains Duplicate 
rev arr 
anagram 
max , min no in an array 
chocolate distribution 
maximum subarray 
stock ~( little gray )
nums disappearing in an array ~( little gray )
first last elem in a sorted array

'''


def soln(arr):
    
    len_n = len(arr)
    res = len_n

    for i in range(len_n):
        res = res + i - arr[i]
    return res


nums= [3,0,1]
print(soln(nums))