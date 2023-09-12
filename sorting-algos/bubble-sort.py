def bubble(arr):
    
    for i in range( len(arr)-1 ):

        for j in range( (len(arr) - i - 1) ):

            if ( arr[j] > arr[j+1] ):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]




arr = [7,8,3,1,2]
bubble(arr)
print(arr)