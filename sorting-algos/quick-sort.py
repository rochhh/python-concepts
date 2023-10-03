def simple_quick_sort(arr):
    
    if len(arr) <= 0:
        return arr

    pivot = arr[0]
    small = []
    big = []

    for n in arr[1:]:

        if n < pivot:
            small.append(n)
        else:
            big.append(n)

    sorted_small = simple_quick_sort(small)
    sorted_big = simple_quick_sort(big)

    return sorted_small + [pivot] + sorted_big



def quick_sort(arr , start , end):

    pivot = arr[start]

    i = 1
    j = len(arr)-1

    while start < end:

        while arr[start] <= pivot:
            i+=1
        
        while arr[end] > pivot:
            j-=1

        if start < end :
            arr[start] , arr[end] = arr[end] , arr[start]

    
    pivot , arr[end] = arr[end] , pivot

    return arr





arr = [5,2,9,1,4,6]

print(quick_sort(arr , 0 , len(arr)-1 ))