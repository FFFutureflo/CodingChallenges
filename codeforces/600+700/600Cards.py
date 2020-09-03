import sys

"""
https://codeforces.com/problemset/problem/1220/A
"""

if __name__ == "__main__":

    n = int(input())
    x = input()

    z = x.count("z")

    n = n - (4*z)
    y = n/3

    answer = []
    while(y >= 1):
        answer.append("1")
        y = y -1
    while(z >= 1):
        answer.append("0")
        z = z-1
    

    answer = " ".join(answer)
    print(answer)
"""
Lies einen Input als Int ein
Lies einen zweiten Input als String ein und splitte ihn in chars
Schaue wie oft z vorkommt
Ziehe z * 4 von dem ersten Input ab
Teile den Rest von Input durch 3 = y
Generiere einen String mit:
z * 1 + y * 0 und trenne die einzelnen Chars durch Leerzeichen
Gib den String aus
"""
