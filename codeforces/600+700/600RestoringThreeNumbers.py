import sys

"""
https://codeforces.com/problemset/problem/1154/A
"""

if __name__ == "__main__":

    numbers = input().split()

    n = []

    for x in numbers:
        n.append(int(x))
    n.sort()

    c = n[3] - n[2]
    b = n[3] - n[1]
    a = n[3] - n[0]

    print(str(c) + " " + str(b) + " " + str(a))


"""
Lies vier Zahlen ein 
Splitte sie in eine List
Sortiere die List nach Größe
Zieh die zweitgrößte von der größten Zahl ab -> c
Zieh die drittgrößte von der größten Zahl ab -> b
Zieh die kleinste von der größten Zahl ab -> a

"""
