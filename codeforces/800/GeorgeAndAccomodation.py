"""
https://codeforces.com/problemset/problem/467/A
"""


def function():
    n = int(input())

    counter = 0

    for _ in range(n):
        p, q = map(int, input().split())
        if (q-p) >= 2:
            counter += 1

    print(counter)


if __name__ == "__main__":
    function()

"""

"""
