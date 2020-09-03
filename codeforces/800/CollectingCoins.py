"""
https://codeforces.com/problemset/problem/1294/A
"""


def function():
    t = int(input())

    read_input = []
    for x in range(0, t):
        read_input.append(input())

    for x in read_input:

        answer = "NO"
        numbers = [int(i) for i in x.split(" ")]
        # take last item and save it in n
        n = numbers.pop()
        maxNumber = max(numbers)

        sum = 0
        for i in numbers:
            sum = sum + maxNumber - i
        if n >= sum and (n-sum) % 3 == 0:
            answer = "YES"

        print(answer)


if __name__ == "__main__":
    function()

"""


Read input t = number of tests

Do the following t times:
    read the next line
    split the input and transform it to integers for variables a, b, c and n
    find the maximum of a, b, c
    sum the differences between a, b and c
    calculate if (n - sum(differences)) % 3 == 0:
        answer = Yes
    else:
        answer = No


"""
