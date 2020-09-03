"""
https://codeforces.com/problemset/problem/266/A
"""


def test_example1():
    result = function(3, "RRG")
    assert result == 1
    
def test_example2():
    result = function(5, "RRRRR")
    assert result == 4

def test_example3():
    result = function(4, "BRBG")
    assert result == 0

def function(n, stones):

    counter = 0
    
    for i in range(1, n):
        if stones[i] == stones[i-1]:
            counter = counter + 1
            
    return counter



if __name__ == "__main__":

    n = int(input())
    stones = input()
    
    result = function(n, stones)
    print(result)
    
"""



"""
