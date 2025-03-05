n = 1234

def count_bits(n):
    return bin(n).count("1")

print(count_bits(n))