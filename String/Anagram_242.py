def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for ch in s:
            if ch not in t:
                return False
        return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))