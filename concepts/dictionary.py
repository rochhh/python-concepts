
dic = {"name":"john" , "age":30 , "lang":["py" , 'java' , "js"] , "name":"mj" , "age":40}

# get a value 

print(dic.get("age"))


# update values 

dic.update({"name":"mj" , "age":20})

# delete 

del dic["age"]


# can also use pop() to do the same 
age_popped =dic.pop("age") 
print(age_popped)
# this will however return the popped value , which we can store in a var 

# length

len(dic)

# view keys , values

dic.keys() , dic.values()

dic.items() # gives both k , v 

# loop a dic

for k , v in dic.items():
    print(k , v)