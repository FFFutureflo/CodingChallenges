import sys

"""
https://codeforces.com/contest/785/problem/A
"""

if __name__ == "__main__":

    n = int(input())

    counter = 0

    for i in range(n):

        x = input()

        if(x == "Tetrahedron"):
            counter = counter + 4
        elif(x == "Cube"):
            counter = counter + 6
        elif(x == "Octahedron"):
            counter = counter + 8
        elif(x == "Dodecahedron"):
            counter = counter + 12
        elif(x == "Icosahedron"):
            counter = counter + 20

    print(counter)
