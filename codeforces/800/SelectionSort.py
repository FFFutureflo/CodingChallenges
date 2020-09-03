"""
https://www.youtube.com/watch?v=nHYmMvIJsVI
"""


def function(numbers):

    orderedList = []
    for x in range(0, len(numbers)):
        minimum = min(numbers)
        orderedList.append(minimum)
        numbers.pop(numbers.index(minimum))

        print(numbers)
        print(orderedList)


def alternative(numbers):

    for x in range(0, len(numbers)):

        i = numbers[x:].index(min(numbers[x:]))
        print(numbers[x:])
        print(i)
        if i != x:
            number = numbers[i]
            numbers[i] = numbers[x]
            numbers[x:][x] = number
        print(numbers)

    print(numbers)


if __name__ == "__main__":
    numbers = [5, 4, 2, 3, 1, 234, 1, 123, 12]
    # function(numbers)
    alternative(numbers)
"""

Schaue durch Liste und suche das kleinste Element
Tausche das kleinste Element mit Element an Position 1
Schaue durch den Rest der Liste und mache das Gleiche

"""
