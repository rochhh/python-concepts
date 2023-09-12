def quick_sort(arr):
    
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

    sorted_small = quick_sort(small)
    sorted_big = quick_sort(big)

    return sorted_small + [pivot] + sorted_big




arr = [5,2,9,1,5,6]

print(quick_sort(arr))