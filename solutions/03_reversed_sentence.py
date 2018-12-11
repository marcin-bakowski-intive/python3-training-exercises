"""
Write a function that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.

Example:
This is a test.

Result:
test. a is This
"""


def reverse_sentence():
    sentence = input("Write a short sentence with multiple words: ")
    print("Reversed words: %s" % sentence[::-1])


reverse_sentence()
