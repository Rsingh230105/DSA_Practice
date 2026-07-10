## TC = o(n)
## SC = o(n)

def check_str_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    # if s2 in (s1 + s1):
    #     return True
    # else:
    #     return False
    return s2 in s1+s1
    
print(check_str_rotation("waterbottle","erbottlewat"))

''' s1 = waterbottle
Right rotation s1 : 1 : ewaterbottl
                 2  : lewaterbott
                   3: tlewaterbot
                   4: ttlewaterbo
                   5. ottlewaterb
                   6. bottlewater
                   7. rbottlewate
                   8. erbottlewat ## this is string 2
                   9. terbottlewa
                   10. aterbottlew
                   11. waterbottle # repeat
                   
                   So, s1+s1 = waterbottlewaterbottle
                      -------> every rotation in (s1+s1) string

left Rotation: waterbottle
                aterbottlew
                terbottlewa
                erbottlewat   ← s2
                rbottlewate
                bottlewater
                ottlewaterb
                ttlewaterbo
                tlewaterbot
                lewaterbott
                ewaterbottl
                waterbottle

                   '''