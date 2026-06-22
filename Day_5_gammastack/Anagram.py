def Anagram(s1,s2):
    
    if len(s1) != len(s2):
        return False
    
    freq = {}
    
    for ch in s1:
        ## dictionary.get(key, default_value)
        ## If key exists → returns its value.
        ##If key does not exist → returns default_value.

        freq[ch] = freq.get(ch, 0) + 1
        
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        
    return all(count == 0 for count in freq.values())

    ## all(iterable) buit in method
    ## if all element are True
    ## if at least one element is False
     
print(Anagram("listen","silent"))
print(Anagram("Hello","World"))