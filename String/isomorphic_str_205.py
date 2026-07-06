

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_stot = {} # mapping s to t
        map_ttos = {} # mapping t to s

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]


            # S to T mapping
            if char_s in map_stot:
                if map_stot[char_s] != char_t:
                    return False
            else:
                map_stot[char_s] = char_t

            # T to S mapping
            if char_t in map_ttos:
                if map_ttos[char_t] != char_s:
                    return False
            else:
                map_ttos[char_t] = char_s
        return True
    

print(Solution().isIsomorphic("egg", "add"))   # True
print(Solution().isIsomorphic("foo", "bar"))   # False
print(Solution().isIsomorphic("paper", "title"))  # True
print(Solution().isIsomorphic("badc", "baba"))    # False

## TC = o(N)
## SC = o(N)