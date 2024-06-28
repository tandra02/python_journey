# You are given a code, assign to function a lambda function that gets one argument and returns True if the argument is not a vowel.
# Vowels are the characters - 'a', 'e', 'i', 'o', 'u'.

iterable = input()
function = lambda strng : strng not in ('a', 'e', 'i', 'o', 'u')

no_vowels = filter(function, iterable)
print(''.join(list(no_vowels)))