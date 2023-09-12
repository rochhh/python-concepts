# more useful for LL than []


def insertion_sort(n):
    
    for i in range(1, len(n)):
        current = n[i]  
        j = i - 1  

        
        while j >= 0 and current < n[j]:
            n[j + 1] = n[j] 
            j -= 1

        n[j + 1] = current


arr = [1,2,4,3]
insertion_sort(arr)

print(arr)