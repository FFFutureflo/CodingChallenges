"""
https://codeforces.com/problemset/problem/41/A
"""


def function():
    a = input()
    b = input()

    if (a == b[::-1]):
        answer = "YES"
    else:
        answer = "NO"

    print(answer)


if __name__ == "__main__":
    function()

"""
Read Input 1 as String a
Read Input 2 as String b
turn b around
if a == b:
    answer = Yes
else:
    ansewr = No
output answer
"""
