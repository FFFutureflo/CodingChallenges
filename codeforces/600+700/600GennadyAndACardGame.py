import sys

"""
https://codeforces.com/problemset/problem/1097/A
"""

if __name__ == "__main__":

    tableCard = input()
    rankTableCard = tableCard[0:1]
    suitTableCard = tableCard[1:2]

    handCards = input().split()

    ranksHandCards = []
    suitsHandCards = []

    for card in handCards:
        ranksHandCards.append(card[0:1])
        suitsHandCards.append(card[1:2])

    answer = "No"

    for x in ranksHandCards:
        if(x == rankTableCard):
            answer = "Yes"

    if(answer != "Yes"):
        for x in suitsHandCards:
            if(x == suitTableCard):
                answer = "Yes"

    print(answer)

"""
Lies die erste Zeile ein
Splitte sie in die zwei chars

Lies die zweite Zeile aus
Splitte die Eingabe in suit und rank

Prüfe ob in suit Array der Suit der ersten Eingabe drin ist
Wenn nicht erfolgreich:
    Prüfe ob in rank arry der rank der ersten Eingabe drin ist
        Wenn nicht erfolgreich:
            Ergebnis = "No"
        Sonst
            Ergebnis = "Yes"
Ergebnis = "Yes"


"""
