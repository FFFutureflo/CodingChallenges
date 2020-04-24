import sys

"""
https://codeforces.com/problemset/problem/136/A
"""

if __name__ == "__main__":

    n = int(input())
    x = input().split()

    x = list(map(int, x))

    answer = ""
    for i in range(1, (n+1)):
        answer = answer + str((x.index(i) + 1))
        if i < n:
            answer = answer + " "

    print(answer)
"""
Read an Int input
Read a second input
Split the input at the spaces
Transform input into Ints
Do a for loop with i from 1 to n + 1:
    get the index of i and write it to a srting
print the string
"""
