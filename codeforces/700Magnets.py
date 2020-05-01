import sys

"""
https://codeforces.com/contest/344/problem/A
"""

if __name__ == "__main__":

    n = int(input())

    magnets = []
    for i in range(1, n + 1):
        magnets.append(input())

    value = magnets[0]
    counter = 1

    for magnet in magnets:
        if magnet != value:
            counter += 1
        value = magnet
    print(counter)

"""
Read n as int input()
Create an empty list
for-loop with range of n + 1
    read magnet as input()
    append magnet to empty list
value = magnets[0]
counter = 1
for magnet in magnets:
    if magnet != value:
        counter += 1
    set value to magnet
print(counter)

"""
