import re

def is_even(x):
    return abs(x) % 2 == 0

user_input = input("Enter a list of numbers separated by commas: ")


def TakeWhile(user_input):
    arr = [float(x) if '.' in x else int(x) for x in re.findall(r'[-+]?\d*\.\d+|\d+', user_input)]

    current_sequence = []
    longest_sequence = []


    for i in arr:
        if is_even(i) == True:
            current_sequence.append(i)

        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = []

    if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence

    return longest_sequence

print(f"The longest sequence of even numbers is: {TakeWhile(user_input)}")