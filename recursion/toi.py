def toi(n , A , B , C):
    
    if n > 0:
    
        toi( n- 1 , A , C , B )
        print(f"Move from-> {A} ,to -> {C}")
        toi( n-1 , B , A , C )


print(toi(3 , 1 , 2 , 3))