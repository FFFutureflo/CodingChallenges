"""
https://codeforces.com/problemset/problem/155/A
"""


def function():
    n = int(input())

    points = list(map(int, input().split()))

    counter = 0

    for i in range(1, n):
        subcounter_highest = 0
        subcounter_lowest = 0
        for a in range(0, i):
            if points[i] > points[a]:
                subcounter_highest = subcounter_highest + 1
            elif points[i] < points[a]:
                subcounter_lowest = subcounter_lowest + 1
        if subcounter_highest == i or subcounter_lowest == i:
            counter = counter + 1

    print(counter)


if __name__ == "__main__":
    function()

"""
Goal: find out how many amazing performances were done
amazing = either all time lowest or all time highest score (until date)
a coder's first contest isn't considered amazing

n = number of contests participated
list separated with spaces = points in contests

algorithm:
- read n as int
- read list of int -> points in contests
- counter = 0
- go through the list of points
    - find out if actual value is either highest or lowest of all time
    - if yes:
        amazing performance -> increase counter
    - if no:
        not an amazing performance
- print out number of amazing performances
"""
