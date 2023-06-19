def add(x,y):
    return x+y

def high( var , add ):
    var_2 = var * add
    print(var_2)
    print(add)
    return var_2

print( high(2 , add(1,3) ) )