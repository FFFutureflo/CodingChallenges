"""
https://codeforces.com/problemset/problem/263/A
"""


def function(array):

    x = [x for x in array if "1" in x][0]

    x_dif = abs(2-array.index(x))
    y_dif = abs(2-x.index("1"))

    moves = x_dif + y_dif

    print(moves)


if __name__ == "__main__":

    i = 0
    array = []
    
    while i < 5:
        row = input().split()
        array.append(row)
        i = i + 1
        print(array)
    """
    array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    """
    function(array)
    
    
"""

Read five lines and save them in a 2D-Array -> 
Get the position of the 1
Get the dif of i and j
Sum the diffs


"""
