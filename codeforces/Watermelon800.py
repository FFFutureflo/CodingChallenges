"""
https://codeforces.com/problemset/problem/4/A
"""


def function(n):

    answer = ""
    if(n % 2 == 0 and n > 2):
        answer = "YES"
    else:
        answer = "NO"

    print(answer)
    return answer


if __name__ == "__main__":
    n = int(input())
    function(n)

"""
Read n as an Int input
If n % 2 == 0 and n > 2:
    YES
else:
    NO
"""
