"""
https://codeforces.com/problemset/problem/1374/A
"""


def function():
    t = int(input())

    for _ in range(0, t):
        x, y, n = map(int, input().split())

        for i in range(n, -1, -1):
            if (i % x) == y:
                print(i)
                break


if __name__ == "__main__":
    function()

"""

"""
