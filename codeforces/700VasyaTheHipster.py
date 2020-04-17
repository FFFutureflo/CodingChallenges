import sys

"""
https://codeforces.com/problemset/problem/581/A
"""

if __name__ == "__main__":

    n = input().split()
    n = list(map(int, n))
    n.sort()

    result = (n[1] - n[0]) // 2

    print(str(n[0]) + " " + str(result))
"""
Lies eine List mit zwei Werten ein
Splitte sie
Wandle sie in ints um
Hol dir den kleinen der beiden Werte
Der Kleine Wert ist Ausgabe Teil 1
Subtrahiere vom großen Wert den kleinen Wert
Rechne das Ergebnis durch 2 (Ganzwertteilung)
Baue das Ergebnis zusammen und gib es aus
"""
