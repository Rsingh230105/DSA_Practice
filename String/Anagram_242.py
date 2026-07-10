def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = {}
        d2 = {}
        
        for ch in s:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] += 1

        for ch in t:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] += 1

        
        
        return d1 == d2

    
            
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))

## short way and best way

def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for ch in s:
            d1[ch] = d1.get(ch, 0) + 1

        for ch in t:
            d2[ch] = d2.get(ch, 0) + 1

        return d1 == d2
    
## TC= o(N)
## SC = o(N)

## method 3
## TC = O(nlogn)
## SC = O(n)

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


## optimal count method
## Time: O(n)
## Space: O(1) (the array always has 26 elements)
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        return all(x == 0 for x in count)