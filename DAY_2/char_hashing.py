# s = "azyxyyzaaaa"
# q = ["d","a","y","x"]

# ## using dictionary
# freq_map = {}
# for i in s:
#     if i in freq_map:
#         freq_map[i] += 1
#     else:
#         freq_map[i] = 1
        
# for i in q:
#     if i in freq_map:
#         print(i,":",freq_map[i])
#     else:
#         print(i,":",0)


### optimal method 2 
## if give constraints 'a'<= s[i] <= 'z'
# s = "azyxyyzaaaa"
# q = ["d","a","y","x"]

# hash_list = [0]*26

# for ch in s:
#     ascii_val = ord(ch)
#     index = ascii_val - ord('a')
#     hash_list[index] += 1
    
# for ch in q:
#     ascii_val = ord(ch)
#     index = ascii_val - ord('a')  ## only given small letter
#     print(f"{ch}: {hash_list[index]}")
    
# ## TC = o(N+M)
# ## SC = o(1)


#### best way

s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

freq = [0] * 26

for ch in s:
    freq[ord(ch) - ord('a')] += 1

for ch in q:
    print(ch,":" ,freq[ord(ch) - ord('a')])