# Iteration - process of traversing through an obj 

# Iterable - an obj in which we can perform iteration
# in its class , it has a iter() FOR EG a = 2 , this is not iterable T = (1,2,3) this is iterable

L = [x for x in range(100000)] 
print(type( iter(L)) )  # iterable output -> <class 'list_iterator>

L = [1,2,3] # Iterable !Iterator
L = iter([1,2,3]) # Iterabl Iterator 

# iterator - obj cus of which iteration happens ->  iter()

#iter() this is iterator 
# next() both next && iter should be present to be an ITERATOR !!!!



# Making your own for-loop 


def self_for_loop(iterable):

    iterator = iter(iterable)

    while True:
        
        try:
            print( next(iterator) )
        except StopIteration:
            break


# making your own range()


class iterable_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return iterator_range(self)

class iterator_range:
    
    def __init__(self , iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start += 1

        return current


for i in iterable_range(1,11):
    print(i)
