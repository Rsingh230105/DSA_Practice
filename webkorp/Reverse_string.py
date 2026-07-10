
## TC = o(n), SC = o(n) ## optimal
def reverse_str(s):
    res = list(s)
    i = 0
    j = len(s)-1
    
    while i<j:
        res[i],res[j] = res[j],res[i]
        i += 1
        j -= 1
    return "".join(res)

print(reverse_str("hello")) 
        
