''' SETS '''

s = {1,2,3,4} # or set(1,2,3,4)

# add single elem 
s.add(5)

#add mulitple elems
s.update([6,7,8])

# remove elem 

s.remove(5)  # s.discard(5) does the same thing

# find same elems from diff sets 

s1 = {1,2,3}
s2 = {3,4,5}
s3 = {3,6,7}

s1.intersection(s2,s3)  # {3}


# similarly with the elems that are diff in sets 
# we use s1.symmetric_difference() !!!!NOTE!!!!!!

s2.symmetric_difference(s1,s3)

# optimal for membership operators ( in , not )
# as the set O(n) -> 1 && mem ops -> O(n)

# hence we can use it to replace the mem ops 