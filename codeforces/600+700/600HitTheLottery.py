import sys

"""
https://codeforces.com/problemset/problem/996/A
"""

if __name__ == "__main__":

    n = int(input())

    counter = 0
    bills = [100, 20, 10, 5, 1]

    for i in bills:
        counter = counter + n // i
        n = n % i

    print(str(counter))
