# Exercise: A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, 
# the sentence: "The quick brown fox jumps over the lazy dog is a pangram, because it uses the letters A-Z at least once" (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]

def pengram_test(pp):
    pengram = True
    l = list(pp)
    for i in b:
        if i not in l:
            pengram = False
            exit

    return pengram

print(pengram_test("the quick brown fox jumps over the lazy dog"))

