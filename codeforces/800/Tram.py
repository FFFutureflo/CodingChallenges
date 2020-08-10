"""
https://codeforces.com/problemset/problem/546/A
"""


def function():
    n = int(input())

    input_array = []
    i_a = []
    while n > 0:
        array_list = list(map(int, input().split()))
        i_a = [array_list[0], array_list[1]]
        input_array.append(i_a)
        n = n - 1

    max_number = 0
    person = 0
    for a in input_array:
        person = person - a[0] + a[1]
        if max_number < person:
            max_number = person

    print(max_number)


if __name__ == "__main__":
    function()

"""
Read Input as int n(number of stops)
Read Input n times:
Read line and save it as two dimensional array
Startnumber = 0
subtract first number of array pair
add second number of array pair
check if number is higher than max_number, if yes, save it
"""
