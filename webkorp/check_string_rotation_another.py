def check_str_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    # if s2 in (s1 + s2):
    #     return True
    # else:
    #     return False
    return s2 in s1+s2
    
print(check_str_rotation("waterbottle","erbottlewat"))