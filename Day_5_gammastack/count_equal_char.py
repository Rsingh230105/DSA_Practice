def count_equal_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq.get('x', 0) == freq.get('o', 0)

print(count_equal_char("xooxoxxo"))  # True