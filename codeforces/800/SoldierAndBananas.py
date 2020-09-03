"""
https://codeforces.com/problemset/problem/546/A
"""


def function():
    k, n, w = map(int, (input().split()))

    costs = 0

    for i in range(1, w+1):
        costs = costs + i * k

    borrow = costs - n
    if borrow < 0:
        borrow = 0
    print(borrow)


if __name__ == "__main__":
    function()

"""
Read Input and split it in 3 integers
- cost of first banana = k
- money of soldier = n
- bananas he wants = w

costs = 1 * k + 2 * k + ... + w * k

borrow = costs - n

if borrow < 0 : borrow = 0

Output money he needs to borrow
"""
