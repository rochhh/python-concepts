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
stock (√)
nums disappearing in an array ~( little gray )
first last elem in a sorted array

'''


def soln(nums):
    buy = 0
    sell = 1
    profit = 0 
    max_profit = 0
    while sell < len(nums):
        profit = nums[sell] - nums[buy]
        max_profit = max(profit , max_profit)

        if nums[sell] < nums[buy]:
            buy = sell
        sell+=1

    return max_profit

nums= [7,6,5,4,3,2,1]

print(soln(nums))
