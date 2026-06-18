# num = int(input("Enter the number:"))

# fac = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         fac.append(i)
# print("Factors of", num, "are:", fac)

#-----
# optimized code
num = int(input("Enter the number:"))
fac = []
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        fac.append(i)
        if i != num // i:
            fac.append(num // i)
            
print("Factors of", num, "are:", fac)