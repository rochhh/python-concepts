def func(n):

    if n == 1 :
        return 1
    if n == 0:
        return 0
    return func(n-1) + func(n-2)


cache = [-1]*500 # global 

def memoFib(n):


    if n <= 1: 
        cache[n] = n
        return n
    
    else:

        if cache[n-1] == -1:
            cache[n-1] = memoFib(n-1)

        if cache[n-2] == -1:
            cache[n-2] == memoFib(n-2)

        return cache[n-2] + cache[n-1]
    



print(memoFib(7)) 