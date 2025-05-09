import sys
import re


def is_palindrome(word):
    return word == word[::-1]


def find_palindromes(filename):
    palindromes = set()
    with open(filename, "r") as f:
        for line in f:
            for word in re.findall(r"\b\w+\b", line):
                word = word.lower()
                if len(word) > 1 and is_palindrome(word):
                    palindromes.add(word)
    for p in palindromes:
        print(p)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome_finder.py <filename>")
    else:
        find_palindromes(sys.argv[1])
