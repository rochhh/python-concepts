def count_sort(nums):
    k = max(nums)
    count_arr = [0]*(k+1)
    sum = 0
    res = nums.copy()
    
    # step 1 -> count the occ of nums[i] and add them in a new arr 

    for i in range(len(nums)):
        count_arr[ nums[i] ] +=1

    # step 2 -> cumilative addition to find the relation between the key as the values of the nums arr 
    #           and the value as the value of the cumilative sum 
    #           eg: count:[ 3,6,10,10,11,12,12,14,15,17 ] 
    #           the above values mean that the nums(sorted):[0,0,0,1,1,1,2,2,2,2...]
    #           the count_arr is showing the index vals , reflects the actual position in the sorted array
    
    for i in range(len(count_arr)):
        sum = count_arr[i] + sum
        # sum = count_arr[i] + count_arr[i-1] just make range(1,len())
        count_arr[i] = sum 
    
    '''
    
    step 3 ->

    Go to the nums[] from i = len(nums)-1
    then consider index , val here as 16(index) , 9(val)
    Goto the count_arr[] to the index 9 ,
    decrement the value at index 9 by 1 , here 17 ( hence 17 - 1 = 16 )
    and add the nums[i] value to the res[] , here at index 16 , add 9 

    The same approach for 2nd loop ; 

    goto nums[], now i -= 1 so , the index , value = 15 , 1 respectively 
    goto count_arr[] index 1 ; and decrement the value at index 1 ( here 6 -1 =5 )
    goto res[] at index 5 and add the nums[] value (1)

    keep decrementing(<-) until you reach 0 
    
    '''

    for index in range(len(nums)-1,-1,-1):
       count_arr[nums[index]] -= 1
       res[count_arr[nums[index]]] = nums[index]
    return f"the og arr -> {nums} and the result is \n -> {res} "
       
nums = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(count_sort(nums))