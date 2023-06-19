'''

def modify(func, num): 
    num = num + 1 # 3 
    return func(num)

def fun(num):
    num = num*2 # 6 
    return num+1 # 7 correct 

print(modify( fun , 2 ))

'''

def decorator(func):
    ''' works like a decorator '''
    print(func.__name__) # feature to view the func  val
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper

@decorator
def func_to_pass_as_args():
    print("inside func_to_pass_as_args ")

print(func_to_pass_as_args())
'''
var_func = decorator(func_to_pass_as_args)
print(var_func())

instead of this syntax we use ->

@decotator
def func_to_pass_as_args() 

'''


def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)    
            else:
                raise TypeError("wrong data type") 
            return inner_wrapper
        return outer_wrapper


@staticmethod(int)
def square(x):
    print(x*x) 

print(square(2))