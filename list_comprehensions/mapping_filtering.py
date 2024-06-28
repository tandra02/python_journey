# Given a list of strings words, calculate a new list where only the first letter of each word is stored if the word is palindrome.
# Store the new list in a variable named new_words.
# A palindrome is a string that remains the same even when read backwards, for example "php".

words = eval(input())  # Don't change this line
new_words = [word[0] for word in words if word == word[::-1]]
print(new_words)
