import sys

"""
https://codeforces.com/problemset/problem/867/A
"""

if __name__ == "__main__":

    string = input()
    length = len(string)

    numberAs = string.count("a")

    if(numberAs > (length/2)):
        print(str(length))
    else:
        print(str(numberAs*2-1))


"""
Lies einen String ein
Hol dir die Länge des Strings
Hol dir die Anzahl an "a"s im String
Wenn Anzahl an "a"s >= Länge/2:
    ergebnis = Länge
Sonst:
    ergebnis = Anzahl "a"s * 2 -1
Gib Ergebnis aus

"""
