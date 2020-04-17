import sys

"""
https://codeforces.com/problemset/problem/200/B
"""

if __name__ == "__main__":

    n = int(input())
    x = input().split()

    x = list(map(int, x))

    sum = 0

    for a in x:
        sum = sum + a

    result = sum / n

    print(result)
"""
Lies einen Input als Int ein
Lies einen zweiten Input als list ein
Splitte die Liste
Wandle die Liste in ints um
Addiere alle Elemente der Liste
Teile das Ergebnis durch den ersten Input
Gib das Ergebnis aus
"""
