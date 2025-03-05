# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# create_phone_number([0, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "06-12345678"


n = [0, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def create_phone_number1(n):
    x = 0
    phone_number = ""
    for i in n:
        x += 1
        phone_number += f"{i}"
        if x == 2:
            phone_number += "-"
        # if x == 6:
        #     phone_number += ""
        if x == 10:
           return phone_number
    
# Betere optie, wist alleen niet dat .format bestond.
def create_phone_number2(n):
    return "{}{}-{}{}{}{}{}{}{}{}".format(*n)

print(create_phone_number1(n))
print(create_phone_number2(n))