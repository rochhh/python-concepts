# simple way of making iterator 

def gen_func():

    yield 1
    yield 2
    yield 3

gen = gen_func()

# print( 1 + next(gen) )

def func(num , gen):
    var =  num + next(gen)
    var2 = var + next(gen)
    var3 = var2 + next(gen)

    return var3 

print( func(1 , gen) ) # ans 7 



# range() using gen 


def gen_range(start ,end):
    for i in range(start,end):
        yield i 


def fn1(num):
    yield num + 1

def fn2(num):
    
    yield 10 * num

print(  next(fn2(next(fn1(10))))  ) # ugly af , for some reason in tutorials theyre not using the next()



