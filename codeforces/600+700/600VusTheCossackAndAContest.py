import sys

"""
https://codeforces.com/problemset/problem/1186/A
"""

if __name__ == "__main__":

    numbers = input().split()
    numbers = list(map(int, numbers))

    if(numbers[0] <= numbers[1] and numbers[0] <= numbers[2]):
        print("Yes")
    else:
        print("No")


"""
Lies einen Input ein
Splitte den Input bei den Leerzeichen
Wandle den Array in einen Int-Array um
Prüfe ob Zahl 2 und Zahl 3 größer gleich Zahl 1 sind
Wenn ja:
    Ausgabe = "Yes"
Wenn nein:
    Ausgabe = "No"
"""
