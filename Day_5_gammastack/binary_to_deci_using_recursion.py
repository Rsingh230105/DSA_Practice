# ## Binary to Decimal + Decimal to Binary using recursion
# """
# Input: binary = "1010" → Output: 10 
# Input: n = 13 → Output: "1101"
# """
# ## Decimal to binary
# def dec_to_bin(n):
#     if n==0:
#         return ""
#     return dec_to_bin(n // 2) + str(n % 2)


# # binary to decimal
# # def bin_to_dec(bin):
# #     return int(bin,2) # built in

# # manual binary to decimal
# def bin_to_dec(b):
#     result, power = 0, 0
#     for bit in reversed(b):
#         result += int(bit) * (2 ** power)
#         power += 1
#     return result

# decimal = bin_to_dec(input("Enter binary number:"))
# binary = dec_to_bin(int(input("Enter the number:")))
    
# print(decimal)
# print(binary)

def bin_to_dec(b):
    i = len(b)
    result = 0
    while i>0:
        
        result += int(2**(i-1))
        i -= 1
    return result

print(bin_to_dec("1010"))
        