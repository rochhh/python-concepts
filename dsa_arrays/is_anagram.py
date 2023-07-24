def is_anagram(s,t):
    return sorted(s) == sorted(t)

print(is_anagram("car","asd"))


def soln(s,t):
    
    freq = [0]*26

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a') ] +=1
        freq[ord(t[i]) - ord('a') ] -=1
    
    for i in range(len(freq)):

        if freq[i] != 0:
            return False 
    return True
s = "roch"
t = "hors"
print(soln(s,t))