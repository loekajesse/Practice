# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.
import re

def find_short(s):
    sx = s.split(" ")
    lengtes = []
    for i in sx:
        y = len(re.sub(r'[^\w]', "", i))
        lengtes.append(y)
    return min(lengtes)


def find_short_best(s):
    return min(len(x) for x in s.split())

s = input("geef de string: ")
print(find_short(s))