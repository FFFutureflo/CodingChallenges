"""
https://codeforces.com/problemset/problem/110/A
"""


def function():
    n = input()

    counter = 0

    for digit in n:
        if digit == "4" or digit == "7":
            counter = counter + 1

    a_counter = 0

    for digit in str(counter):
        if digit == "4" or digit == "7":
            a_counter = a_counter + 1
    if a_counter == len(str(counter)):
        output = "YES"
    else:
        output = "NO"
        
    print(output)


if __name__ == "__main__":
    function()

"""

"""
