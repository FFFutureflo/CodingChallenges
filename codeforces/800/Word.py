"""
https://codeforces.com/problemset/problem/59/A
"""


def function():
    word = input()

    l = len(word)

    counter = 0

    for _ in word:
        if _ >= 'A' and _ <= 'Z':
            counter = counter + 1

    if counter > (l/2):
        print(word.upper())
    else:
        print(word.lower())


if __name__ == "__main__":
    function()

"""

"""
