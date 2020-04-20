import sys

"""
https://codeforces.com/problemset/problem/1077/A
"""

if __name__ == "__main__":

    i = int(input())
    main_list = []
    while(i > 0):
        n = input().split()
        n = list(map(int, n))
        main_list.append(n)
        i = i-1

    for x in main_list:

        k_half = x[2]//2
        a = x[0]
        b = x[1]
        result = 0
        if(x[2] % 2 == 0):
            result = k_half * a - (k_half * b)
        else:
            result = k_half * a - (k_half * b) + a

        print(str(result))


"""
Lies einen int ein
Lies n weitere Inputs ein
Wandle die Inputs in Ints um
Splitte die Inputs und packe sie in eine Liste

Für jeden Input:
    Wenn k % 2 = 0: 
        result = k/2*a - (k/2*b)
    Sonst:
        result = k/2*a - (k/2*b) + a
    Gib das Ergebnis aus
"""
