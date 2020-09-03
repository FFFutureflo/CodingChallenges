import sys

"""
https://codeforces.com/problemset/problem/1315/A
"""

if __name__ == "__main__":

    n = int(input())
    while (n >= 1):

        numbers = input().split()
        a = int(numbers[0])
        b = int(numbers[1])

        x = int(numbers[2])
        y = int(numbers[3])

        x_used = x + 1
        y_used = y + 1
        a_right = a - x_used
        a_left = x_used - 1

        b_upper = y_used - 1
        b_lower = b - y_used

        solutions = []
        solutions.append(a_right * b)
        solutions.append(a_left * b)
        solutions.append(b_upper * a)
        solutions.append(b_lower * a)

        solution = max(solutions)

        print(solution)

        n = n - 1
