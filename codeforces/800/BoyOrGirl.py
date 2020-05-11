"""
https://codeforces.com/problemset/problem/236/A
"""


def function():
    word = input()
    distinct_letters = "".join(set(word))

    length = len(distinct_letters)

    answer = ""

    if(length % 2 == 0):
        answer = "CHAT WITH HER!"
    else:
        answer = "IGNORE HIM!"

    print(answer)


if __name__ == "__main__":
    function()

"""
Read Input as String
Transform input to a set
Get the length of the set
Check if length % 2 == 0:
    answer = "CHAT WITH HER!"
Else:
    answer = "IGNORE HIM!"
Ouput answer
"""
