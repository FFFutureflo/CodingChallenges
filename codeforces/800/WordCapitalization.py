"""
https://codeforces.com/problemset/problem/231/A
"""


def function():
    word = input()
    first_letter = word[0:1]

    print(word.replace(first_letter, first_letter.upper(), 1))


if __name__ == "__main__":
    function()

"""
Read Input as String
Get first letter
Replace first letter with upper letter one time
print string
"""
