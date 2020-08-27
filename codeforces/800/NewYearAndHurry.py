"""
https://codeforces.com/problemset/problem/750/A
"""


def test_function_example1():
    
    value_input = "3 222"
    result = function(value_input)
    assert result == 2


def test_function_example2():
    
    value_input = "4 190"
    result = function(value_input)
    assert result == 4
    assert True
    
    
def test_function_example3():
    
    value_input = "7 1"
    result = function(value_input)
    assert result == 7
    assert True

def function(value_input):

    n, k = map(int,(value_input.split()))

    time_to_midnight = 4 * 60
    
    time_to_solve = time_to_midnight - k
    
    counter = 0
    
    for i in range(1,n+1):
        if time_to_solve - (i*5) >= 0:
            counter = counter + 1
            time_to_solve = time_to_solve - (i * 5)
        
    
    return counter


if __name__ == "__main__":
    function()

"""

"""
