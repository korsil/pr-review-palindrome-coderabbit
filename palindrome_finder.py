import sys
import re


def is_palindrome(word):
    return word == word[::-1]


def clean_word(word):
    # Remove punctuation and numbers
    return "".join(c for c in word if c.isalpha())


def find_palindromes(filename):
    palindromes = set()
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                clean = clean_word(word.lower())
                if len(clean) > 1 and is_palindrome(clean):
                    palindromes.add(clean)
    for p in palindromes:
        print(p)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome_finder.py <filename>")
    else:
        find_palindromes(sys.argv[1])
