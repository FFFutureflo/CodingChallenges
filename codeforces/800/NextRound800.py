"""
https://codeforces.com/problemset/problem/158/A
"""


def function(n, k, list):
    counter = 0
    for number in list:
        if(number >= list[k-1] and number > 0):
            counter += 1
    return counter


if __name__ == "__main__":
    line1 = input().split()
    line1 = list(map(int, line1))
    n = line1[0]
    k = line1[1]

    line2 = input().split()
    line2 = list(map(int, line2))
    answer = function(n, k, line2)
    print(answer)
"""
Read first line
Split the line by space
Set first value as n, set first value as k
Read the second line
Split it and write it to a list
Check how many items in the list are greater or equal than value of list[k]
print the number
"""
