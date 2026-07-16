def to_lower(s):
    l = []
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            l.append(chr(ord(i) + 32))
        else:
            l.append(i)
            
    return "".join(l)

print(to_lower("Hello"))
print(to_lower("HELLO"))
print(to_lower("hello"))

    