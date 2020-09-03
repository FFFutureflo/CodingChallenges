"""
https://codeforces.com/problemset/problem/71/A
"""


def reduce(word):
    length = len(word)
    if length > 10:
        word = f"{word[0:1]}{length-2}{word[-1:]}"
    return word


if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        word = input()
        word = reduce(word)
        print(word)

"""
Read n as an Int input
Do n times:
    read word as string input
    if word is longer than 10 characters:
        word = first character of word + number of characters -2 + last character of word
    print word
"""
