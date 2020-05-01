import sys

"""
https://codeforces.com/problemset/problem/734/A
"""

if __name__ == "__main__":

    n = int(input())
    winners = input()

    count = winners.count("A")

    winner = ""

    if count > (n/2):
        winner = "Anton"
    elif count == (n/2):
        winner = "Friendship"
    else:
        winner = "Danik"

    print(winner)


"""
Read int as input()
Read second line of input and store as string
Check how often "A" is included in the string
If count > (int/2):
    print(Anton)
elif count == (int/2):
    print(Friendship)
else:
    print(Danik)
"""
