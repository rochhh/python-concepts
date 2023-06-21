def power(a,b,c):
    return a+b-c

# takes priority over normal power(2,3) 

# print(power(b=2,a=3)) # output -> 9

def mul(*args):

    prod = 1

    for i in args:
        prod = prod + i
    return prod

print("mul ->" , mul(2,3,4,5))