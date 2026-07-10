
## TC = o(n)
## SC = o(1)

def count_vowel(s):
    vowel = 'aeiouAEIOU'
    ## vowel = {'a','e','i','o','u','A','E','I','O','U'} ##Best approach set
    count = 0
    for ch in s:
        if ch in vowel:
            count += 1
    return count

print(count_vowel("programming"))
            
    