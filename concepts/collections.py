from collections import Counter , namedtuple , deque

a = 'aaaaabbbcc'

my_counter = Counter(a)
#  methods just like normal dict 
print(my_counter) # a:5 , b:3 , c :2 
print(my_counter.items()) 
print(my_counter.keys()) #a,b,c

for i in list(my_counter.elements()):
    print(i)


point = namedtuple( 'Point' , 'x,y' )

p = point(1,3)
p.x = 4 # cant do this , this is immutable 
print(p.x) 

q = deque()

q.append(1)
q.append(2)

q.appendleft(99)

print(q)

q.pop()
q.popleft()

print(q)

q.extend([4,5,6])
q.extendleft([4,5,6])

print(q)
