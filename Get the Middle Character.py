# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.

def middle_char(string):
    mid = list(string)
    if (len(string) % 2) == 0:
        numbers = (mid[(int(len(mid) / 2) - 1)], mid[(int(len(mid) / 2 ))])
    else:
        numbers = mid[(int(len(mid) / 2))]

    return numbers

print(middle_char("testing"))