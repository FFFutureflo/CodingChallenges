import sys

"""
https://codeforces.com/problemset/problem/935/A
"""

if __name__ == "__main__":

    n = int(input())
    solutions = 0
    leader = 1

    n = n - 1

    while(n > 0):
        if(n % leader == 0):
            solutions = solutions + 1
        n = n - 1
        leader = leader + 1
    print(solutions)

"""
Lies eine Zahl n ein
Initialisiere Anzahl an Lösungen mit 0
Initialisiere Anzahl Leader mit 1
Ziehe bei n 1 ab
Mache eine Schleife solange n größer als 0 ist
Prüfe ob n % l = 0 ist
    Wenn ja:
        Erhöhe Anzahl Lösungen um 1
    Reduziere n um eins
    Erhöhe l um 1
Gib Anzahl Lösungen aus
"""
