# Reverse a string
from math import ceil


def reverse_string(char_str):
    return char_str[::-1]

# middle part
def middle_part(char_str):
    if len(char_str) < 3:
        return ""
    return char_str[1 : -1]

# title case
def to_title_case(char_str):
    return char_str.title()

# count vowels
def count_vowels(char_str):
    vowels = ["a", "e", "i", "o", "u"]
    """num_vowels = 0
    for char in char_str:
        if char.lower() in vowels:
            num_vowels += 1"""

    return sum(1 for char in char_str if char.lower() in vowels)

# first and last char
def first_and_last(char_str):
    if len(char_str) <= 1:
        return char_str
    return char_str[0] + char_str[-1]

# lowercase word counts and remove duplicates
def word_counts(char_str):
    words = char_str.lower().split()
    return { word : words.count(word) for word in set(words) }

# remove duplicates
def remove_duplicates(char_str):
    chars = set()
    result = ""
    for c in char_str:
        if c not in chars:
            chars.add(c)
            result += c

    return result

# convert camel case to separate words
def camel_to_words(char_str):
    result = ""
    for c in char_str:
        if c.isupper() and result != "": # only insert space if result is not empty
            result += " "
        result += c
    return result.lower()

# find the longest word in a sentence
def longest_word(char_str):
    if char_str == "":
        return ""
    words = char_str.split()
    return max(words, key=len)

# reverse every second letter
def reverse_every_second(char_str):
    return char_str[::-2]

# swap halves of a word ??
def swap_halves(char_str):
    middle = len(char_str)//2
    return char_str[middle:] + char_str[:middle]

# remove special characters
def remove_special_characters(char_str):
    result = ""
    for char in char_str:
        if char.isalnum():
            result += char
    return result

print(remove_special_characters("hi@123"))
