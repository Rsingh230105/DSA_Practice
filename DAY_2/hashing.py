# ## hashing in python
# ## prestoring value into some datastructure like list/dictionary/set and the fetching it.

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# # m ke sare element n me kitni bar aa rhe hai
# # method 1 : bruth force solution

# for i in m:
#     count = 0
#     for j in n:
#         if i == j:
#             count += 1
#     print(i,"occure in n",count)
    
# ## TC =o(m*n)
# ## SC =o(1)

# # --- method 2
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_list =  [0]*11  ## given  1<=n[i]<=10 constraints

# for i in n:
#     hash_list[i] += 1
    
# for num  in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(num,":",hash_list[num])
     
# ## TC = o(n+m)
# ## SC = o(1)       
        
# ## if using dictionary

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

fre_map = {}

for i in n:
    if i not in fre_map:
        fre_map[i] = 1
    else:
        fre_map[i] += 1
        
for i in m:
    if i in fre_map:
        print(i, ":", fre_map[i])
    else:
        print(i,":", 0)

print(fre_map)
        
        
        
    