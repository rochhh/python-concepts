def func(x, n):
    res = 1
    while n > 0:
        res = 1 + (x / n) * res
        n -= 1
    return res

gres = 1 
# global var ^ 

def recursiveTaylor(x,n):
    
    res = 1

    if n ==0:
        return res

    gres = 1 + (x/n) * gres

    return recursiveTaylor(x,n-1) 

print(func(1,100))
