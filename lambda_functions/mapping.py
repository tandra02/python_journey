# Assign to function a lambda function that gets one argument. If the argument is a vowel then it returns the vowel doubled, otherwise returns the argument unchanged.
# Vowels are the characters - 'a', 'e', 'i', 'o', 'u'.

iterable = input() # Don't change this line
function = lambda strng : strng * 2 if strng in ('a', 'e', 'i', 'o', 'u') else strng

# Don't change below this line
double_vowels = map(function, iterable)
print(''.join(list(double_vowels)))