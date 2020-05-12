"""
https://codeforces.com/problemset/problem/112/A
"""


def function():
    a = input().lower()
    b = input().lower()

    answer = ""

    if(a < b):
        answer = -1
    elif(a > b):
        answer = 1
    else:
        answer = 0

    print(answer)


if __name__ == "__main__":
    function()

"""
Read Input a as String and transform lower case
Read Input b as String and transform lower case

answer = ""

if(a < b):
    answer = -1
elif(b > a):
    answer = 1
else:
    answer = 0
    
print(answer)

"""
