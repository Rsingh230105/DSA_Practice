def firstUniqChar(s: str) -> int:

        # Dictionary to store frequency of each character
        freq = {}

        # First pass: Count occurrences of each character
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        # Second pass: Find the first character
        # whose frequency is exactly 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        # No unique character found
        return -1
    
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))

## TC = o(N)
## SC = o(k)    