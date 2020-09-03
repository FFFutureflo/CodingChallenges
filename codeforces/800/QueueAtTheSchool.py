"""
https://codeforces.com/problemset/problem/266/B
"""


def test_function_example1():
    
    first_line = "5 1"
    second_line = "BGGBG"
    result = function(first_line, second_line)
    assert result == "GBGGB"


def test_function_example2():
    
    first_line = "5 2"
    second_line = "BGGBG"
    result = function(first_line, second_line)
    assert result == "GGBGB"
    
    
def test_function_example3():
    
    first_line = "4 1"
    second_line = "GGGB"
    result = function(first_line, second_line)
    assert result == "GGGB"

def function(first_line, second_line):

    n, t = map(int,(first_line.split()))

    list_string = list(second_line)
    working_string = list(second_line)

    for _ in range(t):
        for i in range(1,n):
            if list_string[i] == "G" and list_string[i-1] == "B":
                working_string[i] = "B"
                working_string[i-1] = "G"
        list_string = working_string.copy()
    return "".join(working_string)




if __name__ == "__main__":
    first_line = "5 1"
    second_line = "BGGBG"
    function(first_line, second_line)

"""

"""
