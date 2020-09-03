import sys

"""
https://codeforces.com/problemset/problem/431/A
"""

if __name__ == "__main__":

    x = input().split()
    x = list(map(int, x))

    y = input()
    counter = []
    counter.append(y.count("1"))
    counter.append(y.count("2"))
    counter.append(y.count("3"))
    counter.append(y.count("4"))

    result = 0
    for i in range(4):
        result = result + x[i] * counter[i]
    print(str(result))


"""
Lies eine Zeile ein
Splitte die Zeile an den Leerzeichen und stecke es in den Array x
Wandle den Array in einen Array von ints um
Lies eine zweite Zeile
Zähle die Häufigkeit der Zahlen 1 bis 4
Berechne Kalorienanzahl = Summe(Häufigkeit * Position Array)
print(Kalorienanzahl) 
"""
