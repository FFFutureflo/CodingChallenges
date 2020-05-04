"""
https://codeforces.com/problemset/problem/231/A
"""


def function():
    n = int(input())
    solution = 0
    for i in range(n):
        line = input().split()
        line = list(map(int, line))
        count = 0
        for number in line:
            count = count + number
        if count >= 2:
            solution += 1
    print(solution)


if __name__ == "__main__":
    function()

"""
Read first line and save it as an integer n
Loop n times:
    Read one line and split the input by spaces
    Count of 1 in list
    if count >= 2:
        there will be a solution

print number of solutions
"""
