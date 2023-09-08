def func(n):
    
    if n == 0 :
        return 1

    return n * func(n-1) 

'''

fact(n)= 1*2*3*4 ..... (n-1) * n

fact(n-1) = 1*2*3*4*...*(n-1)

hence , fact(n) = fact(n-1) * n 


'''


print(func(5))