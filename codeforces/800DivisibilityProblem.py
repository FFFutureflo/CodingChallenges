import sys

"""
https://codeforces.com/problemset/problem/1328/A
"""

if __name__ == "__main__":

    n = int(input())
    while (n >= 1):

        x = input().split()
        a = int(x[0])
        b = int(x[1])

        rest = a % b
        if(rest == 0):
            diff = 0
        else:
            diff = b - rest

        print(diff)
        n = n - 1


"""
Liest einen Int n ein
Laufe die Schleife n mal durch:
    Lies eine Zeile ein
    Splitte die Zeile beim Leerzeichen und speichere die Liste als x
    a = x[0]
    b = x[1]
    rest = a % b
    wenn(rest == 0):
        Differenz = 0
    Sonst:
        Differenz = b - rest
    print(Differenz)
    n = n -1

"""
